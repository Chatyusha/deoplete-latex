import pynvim
import subprocess

@pynvim.plugin
class NvimLaTeXCompile(object):
    def __init__(self, nvim):
        self.nvim = nvim


    @pynvim.command('TestCommand')
    def testcommand(self):
#        self.nvim.command("echo \"test message\"")
        test=self.nvim.eval("g:loaded_deolatex")
        self.nvim.command("echo \"g:loaded_deolatex=\""+str(test))

    @pynvim.command('TypeSet')
    def latexTypeset(self):
        path="/usr/local/texlive/2020/bin/x86_64-linux/latex"
        texCompiler="platex"
        driver="dvipdfmx"
        if self.nvim.eval("exists('g:latex_path')") == 0:
            self.nvim.vars["latex_path"] = path
        if self.nvim.eval("exists('g:latex_compiler')") == 0:
            self.nvim.vars['latex_compiler'] = texCompiler
        if self.nvim.eval("exists('g:latex_driver')") == 0:
            self.nvim.vars['latex_driver'] = driver

        path=self.nvim.eval("g:latex_path")
        texCompiler=self.nvim.eval("g:latex_compiler")
        driver=self.nvim.eval("g:latex_driver")

    @pynvim.command('Tex2pdf')
    def LatexCompile(self):
        path="/usr/local/texlive/2020/bin/x86_64-linux/latex"
        texCompiler="platex"
        driver="dvipdfmx"
        if self.nvim.eval("exists('g:latex_path')") == 0:
            self.nvim.vars["latex_path"] = path
        if self.nvim.eval("exists('g:latex_compiler')") == 0:
            self.nvim.vars['latex_compiler'] = texCompiler
        if self.nvim.eval("exists('g:latex_driver')") == 0:
            self.nvim.vars['latex_driver'] = driver

        path=self.nvim.eval("g:latex_path")
        texCompiler=self.nvim.eval("g:latex_compiler")
        driver=self.nvim.eval("g:latex_driver")
        #self.nvim.command("echo '" + str(path)+"'")

