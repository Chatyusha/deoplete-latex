import pynvim
import subprocess

@pynvim.plugin
class NvimLaTeXCompile(object):
    def __init__(self, nvim):
        self.nvim = nvim
        self.path=""
        self.compiler=""
        self.driver=""

    @pynvim.command('TestCommand')
    def testcommand(self):
#        self.nvim.command("echo \"test message\"")
        test=self.nvim.eval("g:loaded_deolatex")
        self.nvim.command("echo \"g:loaded_deolatex=\""+str(test))

    @pynvim.autocmd('BufRead,BufNewFile', pattern='*.tex,*.bib', sync=True)
    def latexTypeset(self):
        self.path="/usr/local/texlive/2020/bin/x86_64-linux/latex"
        self.compiler="platex"
        self.driver="dvipdfmx"
        if self.nvim.eval("exists('g:latex_path')") == 0:
            self.nvim.vars["latex_path"] = self.path
        if self.nvim.eval("exists('g:latex_compiler')") == 0:
            self.nvim.vars['latex_compiler'] = self.compiler
        if self.nvim.eval("exists('g:latex_driver')") == 0:
            self.nvim.vars['latex_driver'] = self.driver

        self.path=self.nvim.eval("g:latex_path")
        self.compiler=self.nvim.eval("g:latex_compiler")
        self.driver=self.nvim.eval("g:latex_driver")

    @pynvim.command('Tex2pdf')
    def LatexCompile(self):
        fname=self.nvim.eval("expand('%:p')")
        self.nvim.command("echo \"" + fname +"\"")
        #self.nvim.command("echo 'Now Developping ...'")

