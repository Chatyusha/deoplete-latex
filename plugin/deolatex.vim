let s:save_cpo = &cpoptions
set cpoptions&vim

if exists('g:loaded_deolatex')
  finish
endif
let g:loaded_deolatex = 1

noremap [ []<Esc>i
inoremap { {}<Esc>i
inoremap ( ()<Esc>i
inoremap " ""<Esc>i
inoremap ' ''<Esc>i
inoremap $ $$<Esc>i
inoremap \[ \[\]<Esc>hi
inoremap \{ \{\}<Esc>hi

let &cpoptions = s:save_cpo
unlet s:save_cpo
