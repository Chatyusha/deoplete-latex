let s:save_cpo = &cpoptions
set cpoptions&vim

if exists('g:loaded_deolatex')
  finish
endif
let g:loaded_spatab = 1

let &cpoptions = s:save_cpo
unlet s:save_cpo
