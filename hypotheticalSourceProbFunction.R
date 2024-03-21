hypothetical_source_prob = function(cesa, upi, variant_id, 
                                    signature_defs = ces.refset.hg19::ces.refset.hg19$signatures$COSMIC_v3.2$signatures) {
  require('data.table')
  if(! is(cesa, 'CESAnalysis')) {
    stop('cesa should be a CESAnalysis.')
  }
  
  if(! is.character(upi) || length(upi) != 1) {
    stop('upi should be a single Unique_Patient_Identifier')
  }
  if(! upi %in% cesa$samples$Unique_Patient_Identifier) {
    stop('The input upi is not in the CESAnalysis samples table.')
  }
  
  if(! is.character(variant_id) || length(variant_id) != 1) {
    stop('variant_id must be a single cancereffectsizeR-style variant ID')
  }
  
  if(! is.data.frame(signature_defs) && ! is.data.table(signature_defs) ) {
    stop('The input signature_defs should be a matrix (rownames are signatures, colnames are trinucleotide contexts).')
  }
  
  trinuc_contexts = select_variants(cesa, variant_ids = variant_id, include_subvariants = T)[variant_type == 'snv', trinuc_mut]
  
  # For a given sample and trinucleotide context, we can calculate the probability that each signature generated the mutation.
  # Some coding substitutions can be caused by multiple nucleotide substitutions. Therefore, we calculate
  # the probability for each context and then produce a weighted average in accordance with the sample's#
  # relative rates of trinucleotide mutation.
  relative_rate_by_trinuc = cesa$trinuc_rates[Unique_Patient_Identifier == upi, trinuc_contexts, with = F]
  trinuc_source_prob = unlist(relative_rate_by_trinuc / sum(relative_rate_by_trinuc)) # getting a named numeric
  
  # Get signature definitions at the relative trinuc contexts
  sig_defs = signature_defs[, trinuc_contexts, drop = F]
  
  # Get a named numeric of signature weights for the sample
  sbs_weights = unlist(cesa$mutational_signatures$biological_weights[upi, .SD, on = 'Unique_Patient_Identifier', .SDcols = rownames(sig_defs)])
  
  # Multiply each signature's trinuc proportions by signature weight
  weighted_props = as.data.table(sig_defs, keep.rownames = 'signature')
  weighted_props[, (names(sig_defs)) := lapply(.SD, `*`, sbs_weights[signature]), .SDcols = is.numeric]
  
  # Normalize so that signature contributions sum to 1 for each context
  weighted_props[, (names(sig_defs)) := lapply(.SD, function(x) x = x/sum(x)), .SDcols = is.numeric]
  
  # Weight context-specific probabilities by the probabilities that each context occurred
  sbs_prob_by_trinuc = melt(weighted_props, id.vars = 'signature', 
                            variable.name = 'context', variable.factor = FALSE,value.name = 'prob')
  sbs_prob_by_trinuc[, prob := prob * trinuc_source_prob[context]]
  sbs_prob = sbs_prob_by_trinuc[, .(prob = sum(prob)), by = 'signature']
  
  # Format output to match the source_prob table generated mutational_signature_effects() 
  source_output = data.table(variant_id = variant_id, Unique_Patient_Identifier = upi)
  source_output[, (sbs_prob$signature) := lapply(sbs_prob$prob, identity)]
return(source_output[]) }