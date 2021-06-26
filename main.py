from kivy.clock import Clock
from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.taptargetview import MDTapTargetView
from kivymd.uix.list import OneLineAvatarIconListItem, IRightBodyTouch
from kivymd.uix.selectioncontrol import MDCheckbox

# from kivymd.uix.behaviors.
import  pandas as pd
from math import pi, sqrt, sin

from sympy import Symbol, solve

'''----------------------------------------------------------------------------------------------------------------------------------'''
# tabelas de perfis

###### Cantoneira
df_cantoneira = pd.read_excel("cantoneira.xls")
df_cantoneira.index=df_cantoneira['perfil']


###### Perfil Z enrigecido

df_ze= pd.read_excel("perfil_ze.xls")
df_ze.index=df_ze['perfil']

###### Perfil U enrijecido

df_ue= pd.read_excel("perfil_ue.xls")
df_ue.index=df_ue['perfil']



#-----------------------------------------------------------------WIDGETS PERSONALIZADOS------------------------------------------------------------------------------------------------------
class ListItemWithCheckbox(OneLineAvatarIconListItem):
    _no_ripple_effect = True

class RightCheckbox(IRightBodyTouch, MDCheckbox):
    pass



#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



class ContentNavigationDrawer( BoxLayout ):
    Builder.load_string(
        """
<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"

    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height

        Image:
            id: avatar
            source: "dimapp.png"


    ScrollView:



        MDList:
            spacing: 10
            id: md_list
            OneLineIconListItem:
                id:tracao_name
                text: "SOLICITANTE"
                on_press:
                    root.screen_manager.transition=Factory.get('FadeTransition')(duration=0.5)
                on_release:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "solicitante"
                ImageLeftWidget:
                    source: "solicitante.png"



            OneLineIconListItem:
                text: "PROPRIEDADES"
                on_press:
                    root.screen_manager.transition=Factory.get('FadeTransition')(duration=0.5)
                on_release:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "propriedades"

                ImageLeftWidget:
                    source: "propriedades.png"

            OneLineIconListItem:
                text:""

            
            OneLineIconListItem:
                text: "RESULTADOS"
                on_press:
                    root.screen_manager.transition=Factory.get('FadeTransition')(duration=0.5)  
                on_release:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "resultados"                                  
                ImageLeftWidget:
                    source: "resultados.png"                
"""
    )

#-----------------------------------------------------------------TELAS------------------------------------------------------------------------------------------------------

class GerenciadorScreen(ScreenManager):
    pass

class Solicitante(Screen):
    # def __init__(self, **kwargs):
    #     super().__init__( **kwargs )
    #     Clock.schedule_once(self._do_setup)
    def testando(self,*args):
        print(self.parent.parent.ids.area_a_tracao.text)



class Propriedades(Screen):
    pass

class Resultados(Screen):
    pass

class Selecao(Screen):
    pass

class TabelaCantoneira(Screen):
    pass
class TabelaPerfilZe(Screen):
    pass
class TabelaPerfilUe(Screen):
    pass

class Variaveis(Screen):
    pass

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------


class MainApp(MDApp):
    selecionado=0

    def on_start(self):#Criando lista com perfis disponíveis
        self.root.ids.gama_compressao.text='1.2'
        self.root.ids.gama_flexao.text = '1.1'
        self.root.ids.moduloe.text = '20000'
        self.root.ids.modulog.text = '7700'
        self.root.ids.fy.text = '25'
        self.root.ids.fu.text = '40'
        self.root.ids.cb_flexao.text='1'
        self.root.ids.ct_tracao.text='1'
        self.root.ids.kx.text='1'
        self.root.ids.ky.text='1'
        self.root.ids.kz.text='1'


        if self.root.ids.lista_cantoneira.children==[]:
            for i in df_cantoneira.index:
                self.root.ids.lista_cantoneira.add_widget( ListItemWithCheckbox( text=str(i)))
        else:
            pass
        if self.root.ids.lista_perfilue.children==[]:
            for i in df_ue.index:
                self.root.ids.lista_perfilue.add_widget(ListItemWithCheckbox(text =str(i)))

        if self.root.ids.lista_perfilze.children==[]:
            for i in df_ze.index:
                self.root.ids.lista_perfilze.add_widget(ListItemWithCheckbox(text =str(i)))

    def __init__(self,**kwargs):
        self.theme_cls.theme_style = "Dark"
        super().__init__(**kwargs)


    def build(self):
        self.tap_target_view=MDTapTargetView(#Botão de ajuda para seleção de perfil
            widget=self.root.ids.help,
            title_text='Botão "Selecionar Perfil" ',
            description_text='Ao clicar no botão, você poderá selecionar algum dos perfis normatizados pela NBR****',
            widget_position='right_top'
        )

        self.tap_target_view_flexao=MDTapTargetView(#Botão de ajuda para seleção de perfil
            widget=self.root.ids.help_flexao,
            title_text='Botão "Selecionar Perfil" ',
            description_text='Ao clicar no botão, você poderá selecionar algum dos perfis normatizados pela NBR****',
            widget_position='right_top'
        )

    def tap_target_start_compressao(self):
        if self.tap_target_view_compressao.state == 'close':
            self.tap_target_view_compressao.start()
        else:
            self.tap_target_view_compressao.stop()

    def tap_target_start_flexao(self):
        if self.tap_target_view_flexao.state == 'close':
            self.tap_target_view_flexao.start()
        else:
            self.tap_target_view_flexao.stop()

    def tap_target_start(self):
        if self.tap_target_view.state == 'close':
            self.tap_target_view.start()
        else:
            self.tap_target_view.stop()

#---------------------------------Retorno Página-------------------------------------------------------------------
    retorno_pagina=0
    def ida(self):
        if self.root.ids.screen_manager.current=='solicitante':
            self.retorno_pagina=1
        elif self.root.ids.screen_manager.current =='propriedades':
            self.retorno_pagina=3
    def retorno(self):
        if self.retorno_pagina==1:
            self.root.ids.screen_manager.current= 'solicitante'
        elif self.retorno_pagina == 3:
            self.root.ids.screen_manager.current = 'propriedades'

    def imprimindo2(self):
        print('funcionou2')


    def imprimindo(self):
        print(len(self.root.ids.box_selecao.children))

    def preenchimento(self, *kwargs):
        self.selecionado=list(kwargs)[0]
        print('preenchimento')
        try:
            if self.root.ids.gerenciador_tabelas.current=="cantoneira":
                self.root.ids.bw.text=''
                self.root.ids.d.text=''
                self.root.ids.y0.text=''
                self.root.ids.x0.text=''
                #----------------------------------Preenchimento Tração-----------------------------------------------------------------------
                self.root.ids.img.source='perfil_cantoneira.png'
                self.root.ids.img_solicitante.source='perfil_cantoneira.png'
                self.root.ids.area.text=str(df_cantoneira.loc[self.selecionado,'a'])
                self.root.ids.area_an0_tracao.text=str(df_cantoneira.loc[self.selecionado,'a'])
                self.root.ids.area_an_tracao.text=str(df_cantoneira.loc[self.selecionado,'a'])
                #----------------------------------Preenchimento compressão-------------------------------------------------------------------
                self.root.ids.area.text=str(df_cantoneira.loc[self.selecionado,'a'])
                self.root.ids.ix.text=str(df_cantoneira.loc[self.selecionado,'i1'])
                self.root.ids.iw.text=str(df_cantoneira.loc[self.selecionado,'iw'])
                self.root.ids.it.text=str(df_cantoneira.loc[self.selecionado,'it'])
                self.root.ids.rx.text=str(df_cantoneira.loc[self.selecionado,'rx'])
                try:
                    self.root.ids.ry.text = str( df_cantoneira.loc[self.selecionado, 'ry'] )
                except:
                    self.root.ids.ry.text = str( df_cantoneira.loc[self.selecionado, 'rx'] )
                self.root.ids.x0.text=str(df_cantoneira.loc[self.selecionado,'x0'])
                try:
                    self.root.ids.y0.text=str(df_cantoneira.loc[self.selecionado,'y0'])
                except:
                    self.root.ids.y0.text = '0'
                self.root.ids.bf.text=str(df_cantoneira.loc[self.selecionado,'bf'])
                try:
                    self.root.ids.bw.text=str(df_cantoneira.loc[self.selecionado,'bw'])
                except:
                    pass
                self.root.ids.t.text=str(df_cantoneira.loc[self.selecionado,'t'])
                try:
                    self.root.ids.iy.text=str(df_cantoneira.loc[self.selecionado,'i2'])
                except:
                    self.root.ids.iy.text = str( df_cantoneira.loc[self.selecionado, 'ix'] )

                #----------------------------------Preenchimento flexão-------------------------------------------------------------------
                self.root.ids.area.text=str(df_cantoneira.loc[self.selecionado,'a'])
                self.root.ids.ix.text=str(df_cantoneira.loc[self.selecionado,'i1'])
                self.root.ids.iw.text=str(df_cantoneira.loc[self.selecionado,'iw'])
                self.root.ids.it.text=str(df_cantoneira.loc[self.selecionado,'it'])
                self.root.ids.rx.text=str(df_cantoneira.loc[self.selecionado,'rx'])
                try:
                    self.root.ids.ry.text = str( df_cantoneira.loc[self.selecionado, 'ry'] )
                except:
                    self.root.ids.ry.text = str( df_cantoneira.loc[self.selecionado, 'rx'] )
                self.root.ids.x0.text=str(df_cantoneira.loc[self.selecionado,'x0'])
                try:
                    self.root.ids.y0.text=str(df_cantoneira.loc[self.selecionado,'y0'])
                except:
                    self.root.ids.y0.text = '0'
                self.root.ids.bf.text=str(df_cantoneira.loc[self.selecionado,'bf'])
                try:
                    self.root.ids.bw.text=str(df_cantoneira.loc[self.selecionado,'bw'])
                except:
                    pass
                self.root.ids.t.text=str(df_cantoneira.loc[self.selecionado,'t'])
                try:
                    self.root.ids.iy.text=str(df_cantoneira.loc[self.selecionado,'i2'])
                except:
                    self.root.ids.iy.text = str( df_cantoneira.loc[self.selecionado, 'ix'] )
                self.root.ids.wx.text = str( df_cantoneira.loc[self.selecionado, 'wx'] )
                try:
                    self.root.ids.wy.text=str(df_cantoneira.loc[self.selecionado,'wy'])
                except:
                    self.root.ids.wy.text = str( df_cantoneira.loc[self.selecionado, 'wx'] )


            elif self.root.ids.gerenciador_tabelas.current=='perfilue':
                self.root.ids.bw.text=''
                self.root.ids.d.text=''
                self.root.ids.y0.text=''
                self.root.ids.x0.text=''
                self.root.ids.img.source='perfil_ue.png'
                self.root.ids.img_solicitante.source='perfil_ue.png'
                #----------------------------------Preenchimento Tração-----------------------------------------------------------------------
                self.root.ids.area.text=str(df_ue.loc[self.selecionado,'a'])
                self.root.ids.area_an0_tracao.text=str(df_ue.loc[self.selecionado,'a'])
                self.root.ids.area_an_tracao.text=str(df_ue.loc[self.selecionado,'a'])
                #----------------------------------Preenchimento compressão-------------------------------------------------------------------
                self.root.ids.area.text=str(df_ue.loc[self.selecionado,'a'])
                self.root.ids.ix.text=str(df_ue.loc[self.selecionado,'ix'])
                self.root.ids.iw.text=str(df_ue.loc[self.selecionado,'iw'])
                self.root.ids.it.text=str(df_ue.loc[self.selecionado,'it'])
                self.root.ids.rx.text=str(df_ue.loc[self.selecionado,'rx'])
                try:
                    self.root.ids.ry.text = str( df_ue.loc[self.selecionado, 'ry'] )
                except:
                    self.root.ids.ry.text = str( df_ue.loc[self.selecionado, 'rx'] )
                self.root.ids.x0.text=str(df_ue.loc[self.selecionado,'x0'])
                try:
                    self.root.ids.y0.text=str(df_ue.loc[self.selecionado,'y0'])
                except:
                    self.root.ids.y0.text='0'
                self.root.ids.bf.text=str(df_ue.loc[self.selecionado,'bf'])
                try:
                    self.root.ids.bw.text=str(df_ue.loc[self.selecionado,'bw'])
                except:
                    pass
                self.root.ids.t.text=str(df_ue.loc[self.selecionado,'t'])
                self.root.ids.d.text=str(df_ue.loc[self.selecionado,'d'])
                try:
                    self.root.ids.iy.text=str(df_ue.loc[self.selecionado,'iy'])
                except:
                    self.root.ids.iy.text = str( df_ue.loc[self.selecionado, 'ix'] )
                #----------------------------------Preenchimento flexão-------------------------------------------------------------------
                self.root.ids.area.text=str(df_ue.loc[self.selecionado,'a'])
                self.root.ids.ix.text=str(df_ue.loc[self.selecionado,'ix'])
                self.root.ids.iw.text=str(df_ue.loc[self.selecionado,'iw'])
                self.root.ids.it.text=str(df_ue.loc[self.selecionado,'it'])
                self.root.ids.rx.text=str(df_ue.loc[self.selecionado,'rx'])
                try:
                    self.root.ids.ry.text = str( df_ue.loc[self.selecionado, 'ry'] )
                except:
                    self.root.ids.ry.text = str( df_ue.loc[self.selecionado, 'rx'] )
                self.root.ids.x0.text=str(df_ue.loc[self.selecionado,'x0'])
                try:
                    self.root.ids.y0.text=str(df_ue.loc[self.selecionado,'y0'])
                except:
                    self.root.ids.y0.text = '0'
                self.root.ids.bf.text=str(df_ue.loc[self.selecionado,'bf'])
                try:
                    self.root.ids.bw.text=str(df_ue.loc[self.selecionado,'bw'])
                except:
                    pass
                self.root.ids.t.text=str(df_ue.loc[self.selecionado,'t'])
                try:
                    self.root.ids.iy.text=str(df_ue.loc[self.selecionado,'iy'])
                except:
                    self.root.ids.iy.text = str( df_ue.loc[self.selecionado, 'ix'] )
                self.root.ids.wx.text = str( df_ue.loc[self.selecionado, 'wx'] )
                try:
                    self.root.ids.wy.text=str(df_ue.loc[self.selecionado,'wy'])
                except:
                    self.root.ids.wy.text = str( df_ue.loc[self.selecionado, 'wx'] )
                self.root.ids.d.text = str( df_ue.loc[self.selecionado, 'd'] )

            elif self.root.ids.gerenciador_tabelas.current=='perfilze':
                self.root.ids.bw.text=''
                self.root.ids.d.text=''
                self.root.ids.y0.text=''
                self.root.ids.x0.text=''
                #----------------------------------Preenchimento Tração-----------------------------------------------------------------------
                self.root.ids.img.source='perfil_ze.png'
                self.root.ids.img_solicitante.source='perfil_ze.png'
                self.root.ids.area.text=str(df_ze.loc[self.selecionado,'a'])
                self.root.ids.area_an0_tracao.text=str(df_ze.loc[self.selecionado,'a'])
                self.root.ids.area_an_tracao.text=str(df_ze.loc[self.selecionado,'a'])
                #----------------------------------Preenchimento compressão-------------------------------------------------------------------
                self.root.ids.area.text=str(df_ze.loc[self.selecionado,'a'])
                self.root.ids.ix.text=str(df_ze.loc[self.selecionado,'i1'])
                self.root.ids.iw.text=str(df_ze.loc[self.selecionado,'iw'])
                self.root.ids.it.text=str(df_ze.loc[self.selecionado,'it'])
                self.root.ids.rx.text=str(df_ze.loc[self.selecionado,'rx'])
                self.root.ids.bf.text=str(df_ze.loc[self.selecionado,'bf'])
                self.root.ids.t.text=str(df_ze.loc[self.selecionado,'t'])
                self.root.ids.d.text=str(df_ze.loc[self.selecionado,'d'])
                try:
                    self.root.ids.ry.text = str( df_ze.loc[self.selecionado, 'ry'] )
                except:
                    self.root.ids.ry.text = str( df_ze.loc[self.selecionado, 'rx'] )
                try:
                    self.root.ids.x0.text=str(df_ze.loc[self.selecionado,'x0'])
                except:
                    self.root.ids.x0.text = '0'
                try:
                    self.root.ids.y0.text=str(df_ze.loc[self.selecionado,'y0'])
                except:
                    self.root.ids.y0.text='0'
                try:
                    self.root.ids.bw.text=str(df_ze.loc[self.selecionado,'bw'])
                except:
                    pass

                self.root.ids.iy.text=str(df_ze.loc[self.selecionado,'i2'])


                #----------------------------------Preenchimento flexão-------------------------------------------------------------------
                self.root.ids.area.text=str(df_ze.loc[self.selecionado,'a'])
                self.root.ids.ix.text=str(df_ze.loc[self.selecionado,'i1'])
                self.root.ids.iw.text=str(df_ze.loc[self.selecionado,'iw'])
                self.root.ids.it.text=str(df_ze.loc[self.selecionado,'it'])
                self.root.ids.rx.text=str(df_ze.loc[self.selecionado,'rx'])
                try:
                    self.root.ids.ry.text = str( df_ze.loc[self.selecionado, 'ry'] )
                except:
                    self.root.ids.ry.text = str( df_ze.loc[self.selecionado, 'rx'] )
                try:
                    self.root.ids.x0.text=str(df_ze.loc[self.selecionado,'x0'])
                except:
                    self.root.ids.x0.text = '0'
                try:
                    self.root.ids.y0.text=str(df_ze.loc[self.selecionado,'y0'])
                except:
                    self.root.ids.y0.text = '0'
                self.root.ids.bf.text=str(df_ze.loc[self.selecionado,'bf'])
                try:
                    self.root.ids.bw.text=str(df_ze.loc[self.selecionado,'bw'])
                except:
                    pass
                self.root.ids.t.text=str(df_ze.loc[self.selecionado,'t'])

                self.root.ids.iy.text=str(df_ze.loc[self.selecionado,'i2'])

                self.root.ids.wx.text = str( df_ze.loc[self.selecionado, 'wx'] )
                try:
                    self.root.ids.wy.text=str(df_ze.loc[self.selecionado,'wy'])
                except:
                    self.root.ids.wy.text = str( df_ze.loc[self.selecionado, 'wx'] )
                self.root.ids.d.text = str( df_ze.loc[self.selecionado, 'd'] )

        except:
            pass


    """---------------------------------------------------cortante--------------------------------------------------------------------------------"""
    """---------------------------------------------------cortante--------------------------------------------------------------------------------"""
    """---------------------------------------------------cortante--------------------------------------------------------------------------------"""
    """---------------------------------------------------cortante--------------------------------------------------------------------------------"""
    """---------------------------------------------------cortante--------------------------------------------------------------------------------"""

    def cortante(self):
        try:

            fy = float( self.root.ids.fy.text )
            gama=1.1
            t = float( self.root.ids.t.text )
            ri = 0
            if t <= 0.63:
                ri = t
            else:
                ri = 1.5 * t
            if self.root.ids.gerenciador_tabelas.current == "cantoneira":
                bw =float( self.root.ids.bf.text )
                h=bw-ri-t
            elif self.root.ids.gerenciador_tabelas.current == "perfilue" or self.root.ids.gerenciador_tabelas.current == "perfilze":
                bw = float( self.root.ids.bw.text )
                h=bw-2*t-2*ri
            moduloe = float( self.root.ids.moduloe.text )
            esbeltez = h/t
            kv = 5

            vrd=0
            if esbeltez <= 1.08*(moduloe*kv/fy)**0.5:
                vrd = (0.6*fy*h*t)/gama
            elif esbeltez > 1.08*(moduloe*kv/fy)**0.5 and esbeltez <= 1.4*(moduloe*kv/fy)**0.5:
                vrd = ((0.65*t**2)*(moduloe*kv*fy)**0.5)/gama
            elif esbeltez>1.4*(moduloe*kv/fy)**0.5:
                vrd = (0.905*moduloe*kv*t**3)/(h*gama)
            vrd=float(format(vrd,'.4f'))
            self.root.ids.cortante.text=str(vrd)
            if vrd >= float(self.root.ids.vsd.text):
                self.root.ids.cortante.icon_right_color = 0, 255, 0, 1
            else:
                self.root.ids.cortante.icon_right_color = 255, 0, 0, 1
        except:
            pass





    """---------------------------------------------------tracao--------------------------------------------------------------------------------"""
    """---------------------------------------------------tracao--------------------------------------------------------------------------------"""
    """---------------------------------------------------tracao--------------------------------------------------------------------------------"""
    """---------------------------------------------------tracao--------------------------------------------------------------------------------"""
    """---------------------------------------------------tracao--------------------------------------------------------------------------------"""

    def calculo_tracao(self):
        try:
            area_a=float(self.root.ids.area.text)
            area_an0=float(self.root.ids.area_an0_tracao.text)
            area_an=float(float(self.root.ids.area_an_tracao.text))
            fy=float(self.root.ids.fy.text)
            fu=float(self.root.ids.fu.text)
            ct=float(self.root.ids.ct_tracao.text)
            gama1=1.1
            gama2=1.35
            gama3=1.65
            resultado1=area_a*fy/gama1
            resultado2=area_an0*fu/gama2
            resultado3=area_an*fu*ct/gama3
            resultados=[resultado1,resultado2,resultado3]
            resultados.sort()
            resultado_tracao=resultados[0]

            resultado_tracao=float( format( resultado_tracao, '.4f' ) )
            self.root.ids.nrd_tracao.text=str(resultado_tracao)
            if float(self.root.ids.nsd.text) > 0:
                if float(self.root.ids.nrd_tracao.text) >=float(self.root.ids.nsd.text):
                    self.root.ids.nrd_tracao.icon_right_color = 0, 255, 0, 1
                else:
                    self.root.ids.nrd_tracao.icon_right_color = 0, 255, 0, 1
            else:
                pass


        except:
            pass



    """------------------------------------------------------compressao-----------------------------------------------------------------------------"""
    """------------------------------------------------------compressao-----------------------------------------------------------------------------"""
    """------------------------------------------------------compressao-----------------------------------------------------------------------------"""
    """------------------------------------------------------compressao-----------------------------------------------------------------------------"""
    """------------------------------------------------------compressao-----------------------------------------------------------------------------"""
    """------------------------------------------------------compressao-----------------------------------------------------------------------------"""

    def calculo_compressao(self):
            #compressao cantoneira
            #compressao cantoneira
            #compressao cantoneira
            #compressao cantoneira
            #compressao cantoneira
        if self.root.ids.gerenciador_tabelas.current == "cantoneira":
            print( 'cantoneira' )
            try:
                area = float( self.root.ids.area.text )
                moduloe = float( self.root.ids.moduloe.text )
                modulog = float( self.root.ids.modulog.text )
                gama = float( self.root.ids.gama_compressao.text )
                fy = float( self.root.ids.fy.text )
                ix = float( self.root.ids.ix.text )
                iy = float( self.root.ids.iy.text )
                iw = float( self.root.ids.iw.text )
                it = float( self.root.ids.it.text )
                kx = float( self.root.ids.kx.text )
                ky = float( self.root.ids.ky.text )
                kz = float( self.root.ids.kz.text )
                lx = float( self.root.ids.lx.text )
                ly = float( self.root.ids.ly.text )
                lz = float( self.root.ids.lz.text )
                x0 = float( self.root.ids.x0.text )
                y0 = float( self.root.ids.y0.text )
                rx = float( self.root.ids.rx.text )
                ry = float( self.root.ids.ry.text )
                r0 = (rx ** 2 + ry ** 2 + x0 ** 2 + y0 ** 2) ** 0.5
                bf = float( self.root.ids.bf.text )
                t = float( self.root.ids.t.text )
                ri = 0
                if t <= 0.63:
                    ri = t
                else:
                    ri = 1.5 * t

                aef_compressao_assimetrica = None
                esbeltez_compressao_assimetrica = None

                nex = (pi ** 2 * moduloe * ix) / (kx * lx) ** 2
                ney = (pi ** 2 * moduloe * iy) / (ky * ly) ** 2
                nez = (1 / (r0 ** 2)) * ((pi ** 2 * moduloe * iw) / (kz * lz) + (modulog * it))
                nexz = (nex + nez) / (2 * (1 - (x0 / r0) ** 2)) * (
                    1 - (1 - (4 * nex * nez * (1 - (x0 / r0) ** 2)) / (nex + nez) ** 2) ** 0.5)
                # nassi = Symbol( 'nassi' )
                # ne_assimetrico = solve( (r0 ** 2 - y0 ** 2 - x0 ** 2) * nassi ** 3 + (
                #     (-ney * r0 ** 2) + (-nex * r0 ** 2) + (-nez * r0 ** 2) + (ney * x0 ** 2) + (
                #     nex * y0 ** 2)) * nassi ** 2 +
                #                         (nex * ney * r0 ** 2 + ney * nez * r0 ** 2 + nex * nez * r0 ** 2) * nassi - (
                #                             nex * ney * nez * r0 ** 2), nassi )
                # raizes_positivas = []
                # for i in ne_assimetrico:
                #     try:
                #         float( i )
                #         if float( i ) > 0:
                #             raizes_positivas.append( i )
                #     except TypeError:
                #         pass
                # raizes_positivas.sort()
                # ne = raizes_positivas[0]
                print(nex, ney, nez, nexz)
                ncalculadas = [nex, ney, nez, nexz]
                ncalculadas.sort()
                ne = ncalculadas[0]
                ie_reduzido1 = ((area * fy / ne) ** 0.5)
                fator1 = 0
                if ie_reduzido1 <= 1.5:  # Fator de redução número 1
                    fator1 = 0.658 ** ((ie_reduzido1) ** 2)
                elif ie_reduzido1 > 1.5:
                    fator1 = 0.877 / ((ie_reduzido1) ** 2)
                b = bf - t - ri
                sigma = fator1 * fy
                ier_elemento = (b / t) / (0.95 * (0.43 * moduloe / sigma) ** 0.5)
                bef = 0
                aef = 0
                if ier_elemento <= 0.673:
                    bef = b
                    aef = area
                else:
                    bef = b * (1 - (0.22 / ier_elemento)) / (ier_elemento)
                    aef = area - (2 * b - 2 * bef) * t
                ncrd = fator1 * aef * fy / gama
                print(ncrd)
                ncrd = float( format( ncrd, '.4f' ) )
                self.root.ids.nrd_compressao.text=str(ncrd)
                try:
                    if float(self.root.ids.nsd.text) < 0:
                        if float(self.root.ids.nrd_compressao.text) >=(float(self.root.ids.nsd.text)*-1):
                            self.root.ids.nrd_compressao.icon_right_color = 0, 255, 0, 1
                        else:
                            self.root.ids.nrd_compressao.icon_right_color = 0, 255, 0, 1
                    else:
                        pass
                except:
                    pass
            except:
                pass


            #compressao perfil ue
            #compressao perfil ue
            #compressao perfil ue
            #compressao perfil ue
        elif self.root.ids.gerenciador_tabelas.current == "perfilue":
            print( 'perfil u' )
            try:
                area = float( self.root.ids.area.text )
                moduloe = float( self.root.ids.moduloe.text )
                modulog = float( self.root.ids.modulog.text )
                gama = float( self.root.ids.gama_compressao.text )
                fy = float( self.root.ids.fy.text )
                ix = float( self.root.ids.ix.text )
                iy = float( self.root.ids.iy.text )
                iw = float( self.root.ids.iw.text )
                it = float( self.root.ids.it.text )
                kx = float( self.root.ids.kx.text )
                ky = float( self.root.ids.ky.text )
                kz = float( self.root.ids.kz.text )
                lx = float( self.root.ids.lx.text )
                ly = float( self.root.ids.ly.text )
                lz = float( self.root.ids.lz.text )
                x0 = float( self.root.ids.x0.text )
                y0 = float( self.root.ids.y0.text )
                rx = float( self.root.ids.rx.text )
                ry = float( self.root.ids.ry.text )
                r0 = (rx ** 2 + ry ** 2 + x0 ** 2 + y0 ** 2) ** 0.5  # Verificar se é melhor colocar o valor da tabela
                bf = float( self.root.ids.bf.text )
                bw = float( self.root.ids.bw.text )
                t = float( self.root.ids.t.text )
                d = float( self.root.ids.d.text )
                ri = 0
                if t <= 0.63:
                    ri = t
                else:
                    ri = 1.5 * t

                aef_compressao_assimetrica = None
                esbeltez_compressao_assimetrica = None

                nex = (pi ** 2 * moduloe * ix) / (kx * lx) ** 2
                ney = (pi ** 2 * moduloe * iy) / (ky * ly) ** 2
                nez = (1 / (r0 ** 2)) * ((pi ** 2 * moduloe * iw) / (kz * lz) ** 2 + (modulog * it))
                nexz = (nex + nez) / (2 * (1 - (x0 / r0) ** 2)) * (
                        1 - (1 - (4 * nex * nez * (1 - (x0 / r0) ** 2)) / (nex + nez) ** 2) ** 0.5)
                print( nex, ney, nez, nexz )
                ncalculadas = [ney, nexz]
                ncalculadas.sort()
                ne = ncalculadas[0]
                ie_reduzido1 = ((area * fy / ne) ** 0.5)  # Índice de esbeltez reduzido
                fator1 = 0
                if ie_reduzido1 <= 1.5:  # Fator de redução número 1
                    fator1 = 0.658 ** ((ie_reduzido1) ** 2)
                elif ie_reduzido1 > 1.5:
                    fator1 = 0.877 / ((ie_reduzido1) ** 2)

                sigma = fator1 * fy
                # Para o enrijecedor de borda
                b_enrijecedor = d - t - ri
                bef_enrijecedor = 0
                ier_enrijecedor = (b_enrijecedor / t) / (0.95 * (0.43 * moduloe / sigma) ** 0.5)
                if ier_enrijecedor <= 0.673:
                    bef_enrijecedor = b_enrijecedor
                elif ier_enrijecedor > 0.673:
                    bef_enrijecedor = b_enrijecedor * (1 - (0.22 / ier_enrijecedor)) / (ier_enrijecedor)
                # Para a mesa
                b_mesa = bf - 2 * t - 2 * ri
                bef_mesa = 0
                ier_mesa = (b_mesa / t) / (0.623 * (moduloe / sigma) ** 0.5)
                iis = 0
                iia = 0
                if ier_mesa <= 0.673:
                    bef_mesa = b_mesa
                elif ier_mesa > 0.673:
                    iis = (t * bef_enrijecedor ** 3 * sin( 90 * pi / 180 ) ** 2) / 12
                    iia1 = 399 * t ** 4 * (0.487 * ier_mesa - 0.328) ** 3
                    iia2 = t ** 4 * (56 * ier_mesa + 5)
                    if iia1 <= iia2:
                        iia = iia1
                    else:
                        iia = iia2
                    # determinando do valor de n
                    nlista = [(0.582 - 0.122 * ier_mesa), 1 / 3]
                    nlista.sort()
                    n = nlista[1]
                    k = 0
                    if d / b_mesa <= 0.25:
                        klista = [(3.57 * (iis / iia) ** n) + 0.43, 4]
                        k = klista[0]
                    elif d / b_mesa > 0.25 and d / b_mesa <= 0.8:
                        klista = [((iis / iia) ** n * (4.82 - 5 * d / b_mesa) + 0.43), 4]
                        k = klista[0]
                    ier_mesa2 = ((b_mesa / t) / (0.95 * (k * moduloe / sigma) ** 0.5))
                    if ier_mesa2 <= 0.673:
                        bef_mesa = b_mesa
                    elif ier_mesa2 > 0.673:
                        bef_mesa = (b_mesa * (1 - (0.22 / ier_mesa2))) / ier_mesa2

                # para alma
                b_alma = bw - 2 * t - 2 * ri
                ier_alma = (b_alma / t) / (0.95 * (4 * moduloe / sigma))
                bef_alma = 0
                if ier_alma <= 0.673:
                    bef_alma = b_alma
                elif ier_alma > 0.673:
                    bef_alma = (b_alma * (1 - (0.22 / ier_alma))) / ier_alma

                aef = area - (
                        2 * b_enrijecedor - 2 * bef_enrijecedor + 2 * b_mesa - 2 * bef_mesa + b_alma - bef_alma) * t
                ncrd = fator1 * aef * fy / gama
                ncrd = float( format( ncrd, '.4f' ) )
                # print( bef_enrijecedor, bef_mesa, bef_alma, aef )
                print( ncrd )
                self.root.ids.nrd_compressao.text=str(ncrd)
                try:
                    if float(self.root.ids.nsd.text) < 0:
                        if float(self.root.ids.nrd_compressao.text) >=(float(self.root.ids.nsd.text)*-1):
                            self.root.ids.nrd_compressao.icon_right_color = 0, 255, 0, 1
                        else:
                            self.root.ids.nrd_compressao.icon_right_color = 0, 255, 0, 1
                    else:
                        pass
                except:
                    pass

            except:
                pass







            #compressao perfil ze
            #compressao perfil ze
            #compressao perfil ze
            #compressao perfil ze
        elif self.root.ids.gerenciador_tabelas.current == "perfilze":
            print( 'perfil z' )
            try:
                area = float( self.root.ids.area.text )
                moduloe = float( self.root.ids.moduloe.text )
                modulog = float( self.root.ids.modulog.text )
                gama = float( self.root.ids.gama_compressao.text )
                fy = float( self.root.ids.fy.text )
                ix = float( self.root.ids.ix.text )
                iy = float( self.root.ids.iy.text )
                iw = float( self.root.ids.iw.text )
                it = float( self.root.ids.it.text )
                kx = float( self.root.ids.kx.text )
                ky = float( self.root.ids.ky.text )
                kz = float( self.root.ids.kz.text )
                lx = float( self.root.ids.lx.text )
                ly = float( self.root.ids.ly.text )
                lz = float( self.root.ids.lz.text )
                x0 = float( self.root.ids.x0.text )
                y0 = float( self.root.ids.y0.text )
                rx = float( self.root.ids.rx.text )
                ry = float( self.root.ids.ry.text )
                r0 = (rx ** 2 + ry ** 2 + x0 ** 2 + y0 ** 2) ** 0.5  # Verificar se é melhor colocar o valor da tabela
                bf = float( self.root.ids.bf.text )
                bw = float( self.root.ids.bw.text )
                t = float( self.root.ids.t.text )
                d = float( self.root.ids.d.text )
                ri = 0
                if t <= 0.63:
                    ri = t
                else:
                    ri = 1.5 * t

                aef_compressao_assimetrica = None
                esbeltez_compressao_assimetrica = None

                nex = (pi ** 2 * moduloe * ix) / (kx * lx) ** 2
                ney = (pi ** 2 * moduloe * iy) / (ky * ly) ** 2
                nez = (1 / (r0 ** 2)) * ((pi ** 2 * moduloe * iw) / (kz * lz) ** 2 + (modulog * it))
                print( nex, ney, nez )
                ncalculadas = [ney, nex, nez]
                ncalculadas.sort()
                ne = ncalculadas[0]
                ie_reduzido1 = ((area * fy / ne) ** 0.5)  # Índice de esbeltez reduzido
                fator1 = 0
                if ie_reduzido1 <= 1.5:  # Fator de redução número 1
                    fator1 = 0.658 ** ((ie_reduzido1) ** 2)
                elif ie_reduzido1 > 1.5:
                    fator1 = 0.877 / ((ie_reduzido1) ** 2)

                sigma = fator1 * fy
                # Para o enrijecedor de borda
                b_enrijecedor = d - t - ri
                bef_enrijecedor = 0
                ier_enrijecedor = (b_enrijecedor / t) / (0.95 * (0.43 * moduloe / sigma) ** 0.5)
                if ier_enrijecedor <= 0.673:
                    bef_enrijecedor = b_enrijecedor
                elif ier_enrijecedor > 0.673:
                    bef_enrijecedor = b_enrijecedor * (1 - (0.22 / ier_enrijecedor)) / (ier_enrijecedor)
                # Para a mesa
                b_mesa = bf - 2 * t - 2 * ri
                bef_mesa = 0
                ier_mesa = (b_mesa / t) / (0.623 * (moduloe / sigma) ** 0.5)
                iis = 0
                iia = 0
                if ier_mesa <= 0.673:
                    bef_mesa = b_mesa
                elif ier_mesa > 0.673:
                    iis = (t * bef_enrijecedor ** 3 * sin( 90 * pi / 180 ) ** 2) / 12
                    iia1 = 399 * t ** 4 * (0.487 * ier_mesa - 0.328) ** 3
                    iia2 = t ** 4 * (56 * ier_mesa + 5)
                    if iia1 <= iia2:
                        iia = iia1
                    else:
                        iia = iia2
                    # determinando do valor de n
                    nlista = [(0.582 - 0.122 * ier_mesa), 1 / 3]
                    nlista.sort()
                    n = nlista[1]
                    k = 0
                    if d / b_mesa <= 0.25:
                        klista = [(3.57 * (iis / iia) ** n) + 0.43, 4]
                        k = klista[0]
                    elif d / b_mesa > 0.25 and d / b_mesa <= 0.8:
                        klista = [((iis / iia) ** n * (4.82 - 5 * d / b_mesa) + 0.43), 4]
                        k = klista[0]
                    ier_mesa2 = ((b_mesa / t) / (0.95 * (k * moduloe / sigma) ** 0.5))
                    if ier_mesa2 <= 0.673:
                        bef_mesa = b_mesa
                    elif ier_mesa2 > 0.673:
                        bef_mesa = (b_mesa * (1 - (0.22 / ier_mesa2))) / ier_mesa2

                # para alma
                b_alma = bw - 2 * t - 2 * ri
                ier_alma = (b_alma / t) / (0.95 * (4 * moduloe / sigma))
                bef_alma = 0
                if ier_alma <= 0.673:
                    bef_alma = b_alma
                elif ier_alma > 0.673:
                    bef_alma = (b_alma * (1 - (0.22 / ier_alma))) / ier_alma

                aef = area - (
                        2 * b_enrijecedor - 2 * bef_enrijecedor + 2 * b_mesa - 2 * bef_mesa + b_alma - bef_alma) * t
                ncrd = fator1 * aef * fy / gama
                # print( bef_enrijecedor, bef_mesa, bef_alma, aef )
                print( ncrd )
                ncrd = float( format( ncrd, '.4f' ) )
                self.root.ids.nrd_compressao.text=str(ncrd)
                try:
                    if float(self.root.ids.nsd.text) < 0:
                        if float(self.root.ids.nrd_compressao.text) >=(float(self.root.ids.nsd.text)*-1):
                            self.root.ids.nrd_compressao.icon_right_color = 0, 255, 0, 1
                        else:
                            self.root.ids.nrd_compressao.icon_right_color = 0, 255, 0, 1
                    else:
                        pass
                except:
                    pass

            except:
                pass


    """---------------------------------------------------------flexao--------------------------------------------------------------------------"""
    """---------------------------------------------------------flexao--------------------------------------------------------------------------"""
    """---------------------------------------------------------flexao--------------------------------------------------------------------------"""
    """---------------------------------------------------------flexao--------------------------------------------------------------------------"""
    """---------------------------------------------------------flexao--------------------------------------------------------------------------"""
    """---------------------------------------------------------flexao--------------------------------------------------------------------------"""

    def calculo_flexao(self):
        if self.root.ids.gerenciador_tabelas.current == "cantoneira":
            pass
#     try:
        #         print('flexao cantoneira')
        #
        #         area = float( self.root.ids.area.text )
        #         moduloe = float( self.root.ids.moduloe.text )
        #         modulog = float( self.root.ids.modulog.text )
        #         gama = float( self.root.ids.gama_flexao.text )
        #         fy = float( self.root.ids.fy.text )
        #         cb = float( self.root.ids.cb_flexao.text )
        #         ix = float( self.root.ids.ix.text )
        #         iy = float( self.root.ids.iy.text )
        #         iw = float( self.root.ids.iw.text )
        #         it = float( self.root.ids.it.text )
        #         kx = float( self.root.ids.kx.text )
        #         ky = float( self.root.ids.ky.text )
        #         kz = float( self.root.ids.kz.text )
        #         lx = float( self.root.ids.lx.text )
        #         ly = float( self.root.ids.ly.text )
        #         lz = float( self.root.ids.lz.text )
        #         x0 = float( self.root.ids.x0.text )
        #         y0 = float( self.root.ids.y0.text )
        #         rx = float( self.root.ids.rx.text )
        #         ry = float( self.root.ids.ry.text )
        #         r0 = (rx ** 2 + ry ** 2 + x0 ** 2 + y0 ** 2) ** 0.5
        #         bf = float( self.root.ids.bf.text )
        #         t = float( self.root.ids.t.text )
        #         wx= float(self.root.ids.wx.text)
        #         ri = 0
        #         if t <= 0.63:
        #             ri = t
        #         else:
        #             ri = 1.5 * t
        #
        #         """-------------------início do escoamento-----------------"""
        #
        #         #largura efetiva
        #         b= bf-ri-t
        #         #caso d AL com psi = 0
        #         k = 0.57
        #         ier = (b / t) / (0.95 * (k * moduloe / fy) ** 0.5)
        #         bef = 0
        #         if ier <= 0.673:
        #             bef = b
        #         elif ier > 0.673:
        #             bef = b * (1 - (0.22 / ier)) / (ier)
        #         lret = b - bef
        #         aret = lret*t
        #         aef =area-aret
        #         #momento de inércia retirado aproximado
        #         ixret= ((t/sin(45*pi/180))*((lret)*sin(45*pi/180))**3)/12 + aret*((bf-lret/2)*sin(45*pi/180))**2
        #
        #         #rebaixo do baricentro devido a retirada da área
        #         y=(aret/aef)*((b-lret/2)*sin(45*pi/180))
        #         yg=bf*sin(45*pi/180)+y
        #
        #         #propriedades efetivas
        #         ixef=ix-ixret
        #         ixg = ixef-aef*y**2
        #         wef = ixg/yg
        #         mrd = wef*fy/gama
        #
        #
        #         """----------------------------Instabilidade lateral com torção------------------------------"""
        #         ney = (pi ** 2 * moduloe * iy) / (ky * ly) ** 2
        #         nez = (1 / (r0 ** 2)) * ((pi ** 2 * moduloe * iw) / (kz * lz) ** 2 + (modulog * it))
        #         me = cb * r0 * (ney * nez) ** 0.5
        #         wc = ix/(bf*sin(45*pi/180))
        #         ier_instabilidade_torcao = (wc*fy/me)**0.5
        #         fator_flt=0
        #         if ier_instabilidade_torcao <= 0.6:
        #             fator_flt = 1
        #         elif ier_instabilidade_torcao > 0.6 and ier_instabilidade_torcao < 1.336:
        #             fator_flt = 1.11 * (1 - 0.278 * ier_instabilidade_torcao ** 2)
        #         elif ier_instabilidade_torcao >= 1.336:
        #             fator_flt = 1 / (ier_instabilidade_torcao ** 2)
        #         sigma_flt=fator_flt*fy
        #         #larguras efetivas devido à instabilidade lateral com torção
        #         k_flt = 0.57
        #         ier_flt = (b/t)/(0.95*(k_flt*moduloe/sigma_flt)**0.5)
        #         bef_flt = 0
        #         if ier_flt <= 0.673:
        #             bef_flt = b
        #         elif ier_flt > 0.673:
        #             bef_flt = b * (1 - (0.22 / ier_flt)) / (ier_flt)
        #
        #
        #         #área retirada
        #         lret_flt = b - bef_flt
        #         aret_flt = lret_flt*t
        #         aef_flt = area - aret_flt
        #         #momento de inércia a retirar
        #         ixret_flt = ((t / sin( 45 * pi / 180 )) * (lret_flt) * sin( 45 * pi / 180 ) ** 3) / 12 + aret_flt * ((bf - lret_flt / 2) * sin( 45 * pi / 180 )) ** 2
        #
        #         #rebaixo do baricentro
        #         y_flt=(aret_flt/aef_flt)*((b-lret_flt/2)*sin(45*pi/180))
        #         yg_flt=bf*sin(45*pi/180)+y_flt
        #
        #         #propriedades efetivas
        #         ixef_flt=ix-ixret_flt
        #         ixg_flt = ixef_flt-aef_flt*y_flt**2
        #         wcef = ixg_flt/yg_flt
        #         mrd_flt = fator_flt*wcef*fy/gama
        #         print(fator_flt, aef_flt, aef, ixef_flt, ixef, wcef,wef, yg_flt)
        #         print(ix)
        #         print(mrd, mrd_flt )
        #         print(y, y_flt, yg, yg_flt)
        #
        #         mrd_resultado_lista=[mrd, mrd_flt]
        #         mrd_resultado_lista.sort()
        #         mrd_resultado = mrd_resultado_lista[0]
        #         mrd_resultado = float( format( mrd_resultado, '.4f' ) )
        #         self.root.ids.mrd_flexao.text=str(mrd_resultado)
        #         self.root.ids.mrd_escoamento.text=str(mrd)
        #
        #         try:
        #             if float(self.root.ids.mrd_flexao.text) >=float(self.root.ids.msd.text):
        #                 self.root.ids.mrd_flexao.icon_right_color = 0, 255, 0, 1
        #             else:
        #                 self.root.ids.mrd_flexao.icon_right_color = 0, 255, 0, 1
        #         except:
        #             pass
        #
        #     except:
        #         pass

            ###perfil ue
            ###perfil ue
            ###perfil ue
            ###perfil ue
            ###perfil ue
            ###perfil ue
        elif self.root.ids.gerenciador_tabelas.current == "perfilue":

            try:
                print('flexão ue')

                gama = float( self.root.ids.gama_flexao.text )
                area = float( self.root.ids.area.text )
                moduloe = float( self.root.ids.moduloe.text )
                modulog = float( self.root.ids.modulog.text )
                fy = float( self.root.ids.fy.text )
                cb = float( self.root.ids.cb_flexao.text )
                ix = float( self.root.ids.ix.text )
                iy = float( self.root.ids.iy.text )
                wx = float( self.root.ids.wx.text )
                wy = float( self.root.ids.wy.text )
                iw = float( self.root.ids.iw.text )
                it = float( self.root.ids.it.text )
                kx = float( self.root.ids.kx.text )
                ky = float( self.root.ids.ky.text )
                kz = float( self.root.ids.kz.text )
                lx = float( self.root.ids.lx.text )
                ly = float( self.root.ids.ly.text )
                lz = float( self.root.ids.lz.text )
                x0 = float( self.root.ids.x0.text )
                y0 = float( self.root.ids.y0.text )
                rx = float( self.root.ids.rx.text )
                ry = float( self.root.ids.ry.text )
                r0 = (rx ** 2 + ry ** 2 + x0 ** 2 + y0 ** 2) ** 0.5  # Verificar se é melhor colocar o valor da tabela
                bf = float( self.root.ids.bf.text )
                bw = float( self.root.ids.bw.text )
                t = float( self.root.ids.t.text )
                d = float( self.root.ids.d.text )
                ri = 0
                if t <= 0.63:
                    ri = t
                else:
                    ri = 1.5 * t
                # início do escoamento

                # ----larguras efetivas
                # Enrijecedor
                b_enrijecedor = d - t - ri
                teste = b_enrijecedor / t
                sigma1 = (bw / 2 - t - ri) * fy / (bw / 2)
                sigma2 = (bw / 2 - d) * fy / (bw / 2)
                sigma3 = (sigma1 + sigma2) / 2
                psi_enrijecedor = (sigma2 / sigma1)  # elemento comprimido com compressão variável
                k_enrijecedor = 0.578 / (psi_enrijecedor + 0.34)
                ier_enrijecedor = (b_enrijecedor / t) / (0.95 * (k_enrijecedor * moduloe / sigma1) ** 0.5)
                bef_enrijecedor = 0
                if ier_enrijecedor <= 0.673:
                    bef_enrijecedor = b_enrijecedor
                elif ier_enrijecedor > 0.673:
                    bef_enrijecedor = b_enrijecedor * (1 - (0.22 / ier_enrijecedor)) / (ier_enrijecedor)
                # área retirada do perfil
                lret_enrijecedor = b_enrijecedor - bef_enrijecedor
                aret_enrijecedor = lret_enrijecedor * t
                aef = area - aret_enrijecedor

                # momento de inércia da parte a retirar
                ixret_enrijecedor = (t * lret_enrijecedor ** 3) / 12 + aret_enrijecedor * (
                    bw / 2 - t - ri - lret_enrijecedor / 2) ** 2
                y_enrijecedor = aret_enrijecedor / aef * (bw / 2 - t - ri - lret_enrijecedor / 2)
                yg = bw / 2 + y_enrijecedor

                # Mesa
                b_mesa = bf - 2 * t - 2 * ri
                bef_mesa = 0
                ier_mesa = (b_mesa / t) / (0.623 * (moduloe / fy) ** 0.5)
                iis = 0
                iia = 0
                if ier_mesa <= 0.673:
                    bef_mesa = b_mesa
                elif ier_mesa > 0.673:
                    iis = (t * bef_enrijecedor ** 3 * sin( 90 * pi / 180 ) ** 2) / 12
                    iia1 = 399 * t ** 4 * (0.487 * ier_mesa - 0.328) ** 3
                    iia2 = t ** 4 * (56 * ier_mesa + 5)
                    if iia1 <= iia2:
                        iia = iia1
                    else:
                        iia = iia2
                    # determinando do valor de n
                    nlista = [(0.582 - 0.122 * ier_mesa), 1 / 3]
                    nlista.sort()
                    n = nlista[1]
                    k_mesa = 0
                    if d / b_mesa <= 0.25:
                        k_mesalista = [(3.57 * (iis / iia) ** n) + 0.43, 4]
                        k_mesalista.sort()
                        k_mesa = k_mesalista[0]
                    elif d / b_mesa > 0.25 and d / b_mesa <= 0.8:
                        k_mesalista = [((iis / iia) ** n * (4.82 - 5 * d / b_mesa) + 0.43), 4]
                        k_mesalista.sort()
                        k_mesa = k_mesalista[0]
                    ier_mesa2 = ((b_mesa / t) / (0.95 * (k_mesa * moduloe / fy) ** 0.5))
                    if ier_mesa2 <= 0.673:
                        bef_mesa = b_mesa
                    elif ier_mesa2 > 0.673:
                        bef_mesa = (b_mesa * (1 - (0.22 / ier_mesa2))) / ier_mesa2

                # área retirada do perfil
                lret_mesa = b_mesa - bef_mesa
                aret_mesa = lret_mesa * t
                aef = aef - aret_mesa

                # momento de inércia do trecho retirado
                ixret_mesa = (lret_mesa * t ** 3) / 12 + aret_mesa * (bw / 2 - t / 2) ** 2
                # rebaixo do baricentro devido à retirada da mesa

                yret_mesa = aret_mesa / aef * (bw / 2 - t / 2)
                yg = yg + yret_mesa

                # alma
                b_alma = bw - 2 * t - 2 * ri
                teste_alma = b_alma / t
                sigma1_alma = (yg - t - ri) * fy / yg
                sigma2_alma = (bw - yg - t - ri) * fy / yg
                psi_alma = sigma2_alma / sigma1_alma * (-1)
                # coeficiente de flmabagem

                k_alma = 4 + 2 * (1 - psi_alma) ** 3 + 2 * (1 - psi_alma)
                # índice de esbeltez do elemento
                ier_alma = (b_alma / t) / (0.95 * (k_alma * moduloe / sigma1) ** 0.5)
                bef_alma = 0
                if ier_alma <= 0.673:
                    bef_alma = b_alma
                elif ier_alma > 0.673:
                    bef_alma = (b_alma * (1 - (0.22 / ier_alma))) / ier_alma

                lret_alma = b_alma - bef_alma
                aret_alma = lret_alma * t
                aef = aef - aret_alma

                # momento de inércia da parte a retirar
                ixret_alma = (t * lret_alma ** 3) / 12 + aret_alma * (bw / 2 - t - ri - lret_alma / 2) ** 2
                y_alma = aret_alma / aef * (bw / 2 - t - ri - lret_alma / 2)
                yg = yg + y_alma
                ixef = ix - ixret_enrijecedor - ixret_mesa - ixret_alma
                # translação do momento de inércia em relação ao eixo que passa pelo CG da seção original para o eixo que passa pelo CG da seção efetiva
                ixg = ixef - aef * (yg - bw / 2) ** 2
                wef = ixg / yg

                # Momento resistente ao escoamento
                mrd = wef * fy / gama

                # print("enrijecedor",sigma1,sigma2,sigma3,k_enrijecedor,ier_enrijecedor, aret_enrijecedor,ixret_enrijecedor)
                # print("mesa",b_mesa, ier_mesa,iia,iis, ier_mesa2,k_mesa,bef_mesa,lret_mesa,aret_mesa, ixret_mesa)
                # print('alma', b_alma, ier_alma,k_alma,bef_alma,lret_alma,aret_alma,ixret_alma)
                # print(mrd)

                """----------------------------------------------------------------------------------------------------------------"""
                # Estado limite de instabilidade lateral com torção
                ney = (pi ** 2 * moduloe * iy) / (ky * ly) ** 2
                nez = (1 / (r0 ** 2)) * ((pi ** 2 * moduloe * iw) / (kz * lz) ** 2 + (modulog * it))
                me = cb * r0 * (ney * nez) ** 0.5
                ier_instabilidade_torcao = (wx * fy / me) ** 0.5
                fator_flt = 0
                if ier_instabilidade_torcao <= 0.6:
                    fator_flt = 1
                elif ier_instabilidade_torcao > 0.6 and ier_instabilidade_torcao < 1.336:
                    fator_flt = 1.11 * (1 - 0.278 * ier_instabilidade_torcao ** 2)
                elif ier_instabilidade_torcao >= 1.336:
                    fator_flt = 1 / (ier_instabilidade_torcao ** 2)
                # cálculo das larguras efetivas ma tensão Xflt*fy
                sigma_flt = fator_flt * fy
                # enrijecedor de borda
                sigma1_flt_enrijecedor = (bw / 2 - t - ri) * (sigma_flt) / (bw / 2)
                sigma2_flt_enrijecedor = (bw / 2 - d) * sigma_flt / (bw / 2)
                sigma3_flt_enrijecedor = (sigma1_flt_enrijecedor + sigma2_flt_enrijecedor) / 2
                psi_flt_enrijecedor = sigma2_flt_enrijecedor / sigma1_flt_enrijecedor
                """O elemento está comprimido com tensões variáveis"""
                k_flt_enrijecedor = 0.578 / (psi_flt_enrijecedor + 0.34)
                ier_flt_enrijecedor = (b_enrijecedor / t) / (
                    0.95 * (k_flt_enrijecedor * moduloe / sigma1_flt_enrijecedor) ** 0.5)
                bef_flt_enrijecedor = 0
                if ier_flt_enrijecedor <= 0.673:
                    bef_flt_enrijecedor = b_enrijecedor
                elif ier_flt_enrijecedor > 0.673:
                    bef_flt_enrijecedor = b_enrijecedor * (1 - (0.22 / ier_flt_enrijecedor)) / (ier_flt_enrijecedor)

                    # área retirada do perfil
                lret_flt_enrijecedor = b_enrijecedor - bef_flt_enrijecedor
                aret_flt_enrijecedor = lret_flt_enrijecedor * t
                aef_flt = area - aret_flt_enrijecedor
                # momento de inpercia da parte a retirar
                ixret_flt_enrijecedor = (t * lret_flt_enrijecedor ** 3) / 12 + aret_flt_enrijecedor * (
                    bw / 2 - t - ri - lret_flt_enrijecedor / 2) ** 2
                # Rebaixo do baricentro
                y_flt_enrijecedor = aret_flt_enrijecedor / aef_flt * (bw / 2 - t - ri - lret_flt_enrijecedor / 2)
                yg_flt = bw / 2 + y_flt_enrijecedor

                # mesa comprimida
                ier_flt_mesa = (b_mesa / t) / (0.623 * (moduloe / sigma_flt) ** 0.5)
                bef_flt_mesa = 0
                is_flt = 0
                ia_flt = 0
                if ier_flt_mesa <= 0.673:
                    bef_flt_mesa = b_mesa
                elif ier_flt_mesa > 0.673:
                    is_flt = (t * bef_flt_enrijecedor ** 3 * sin( 90 * pi / 180 ) ** 2) / 12
                    ia_flt_list = [399 * t ** 4 * (0.487 * ier_flt_mesa - 0.328) ** 3, t ** 4 * (56 * ier_mesa + 5)]
                    ia_flt_list.sort()
                    ia_flt = ia_flt_list[0]
                    # determinqando o valor de n
                    n_flt_lista = [(0.582 - 0.122 * ier_flt_mesa), 1 / 3]
                    n_flt_lista.sort()
                    n_flt = n_flt_lista[1]
                    k_flt_mesa = 0
                    if d / b_mesa <= 0.25:
                        k_flt_mesa_lista = [(3.57 * (is_flt / ia_flt) ** n_flt) + 0.43, 4]
                        k_flt_mesa_lista.sort()
                        k_flt_mesa = k_flt_mesa_lista[0]
                    elif d / b_mesa > 0.25 and d / b_mesa <= 0.8:
                        k_flt_mesa_lista = [((is_flt / ia_flt) ** n_flt * (4.82 - 5 * d / b_mesa) + 0.43), 4]
                        k_flt_mesa_lista.sort()
                        k_flt_mesa = k_flt_mesa_lista[0]
                    ier_flt_mesa2 = ((b_mesa / t) / (0.95 * (k_flt_mesa * moduloe / sigma_flt) ** 0.5))
                    if ier_flt_mesa2 <= 0.673:
                        bef_flt_mesa = b_mesa
                    elif ier_flt_mesa2 > 0.673:
                        bef_flt_mesa = (b_mesa * (1 - (0.22 / ier_flt_mesa2))) / ier_flt_mesa2

                # área retirada do perfil
                lret_flt_mesa = b_mesa - bef_flt_mesa
                aret_flt_mesa = lret_flt_mesa * t
                aef_flt = aef_flt - aret_flt_mesa
                # Momento de inécia do trecho retirado
                ixret_flt_mesa = (lret_flt_mesa * t ** 3) / 12 + aret_flt_mesa * (bw / 2 - t / 2) ** 2
                # rebaixo do  baricentro
                y_flt_mesa = aret_flt_mesa / aef_flt * (bw / 2 - t / 2)
                yg_flt = yg_flt + y_flt_mesa

                # alma
                teste_flt_alma = b_alma / t
                sigma1_flt_alma = sigma_flt * (yg_flt - t - ri) / yg_flt
                sigma2_flt_alma = sigma_flt * (bw - yg_flt - t - ri) / yg_flt
                psi_flt_alma = sigma2_flt_alma / sigma1_flt_alma * (-1)
                k_flt_alma = 4 + 2 * (1 - psi_flt_alma) ** 3 + 2 * (1 - psi_flt_alma)
                ier_flt_alma = (b_alma / t) / (0.95 * (k_flt_alma * moduloe / sigma1_flt_alma) ** 0.5)
                bef_flt_alma = 0
                if ier_flt_alma <= 0.673:
                    bef_flt_alma = b_alma
                elif ier_flt_alma > 0.673:
                    bef_flt_alma = (b_alma * (1 - (0.22 / ier_flt_alma))) / ier_flt_alma

                # área retirada da alma
                lret_flt_alma = b_alma - bef_flt_alma
                aret_flt_alma = lret_flt_alma * t
                aef_flt = aef_flt - aret_flt_alma

                # momento de inércia da parte a retirar
                bef1_flt_alma = 0
                bef2_flt_alma = 0
                if psi_flt_alma > (-0.236) and psi_flt_alma < 0:
                    bef1_flt_alma = bef_flt_alma / (3 - psi_flt_alma)
                    bef2_flt_alma = bef_flt_alma - bef1_flt_alma
                elif psi_flt_alma <= (-0.236):
                    bef1_flt_alma = bef_flt_alma / (3 - psi_flt_alma)
                    bef2_flt_alma = 0.5 * bef_flt_alma

                ixret_flt_alma = (t * lret_flt_alma ** 3) / 12 + aret_flt_alma * (
                    yg_flt - t - ri - bef1_flt_alma - lret_alma / 2) ** 2
                # rebaixo do baricentro
                y_flt_alma = aret_flt_alma / aef_flt * (yg_flt - t - ri - lret_flt_alma / 2)
                yg_flt = yg_flt + y_flt_alma
                ixef_flt = ix - ixret_flt_enrijecedor - ixret_flt_mesa - ixret_flt_alma
                # translação do momento de inércia em relação ao eixo que passa pelo cg
                ixg_flt = ixef_flt - aef_flt * (yg_flt - bw / 2) ** 2
                wcef = ixg_flt / yg_flt

                # Momento resistente à instabilidade por torção
                mrd_flt = sigma_flt * wcef / gama
                print( is_flt, ia_flt, bef_flt_mesa, mrd, mrd_flt )

                mrd_resultado_lista = [mrd, mrd_flt]
                mrd_resultado_lista.sort()
                mrd_resultado = mrd_resultado_lista[0]
                mrd_resultado = float( format( mrd_resultado, '.4f' ) )
                self.root.ids.mrd_flexao.text = str( mrd_resultado )
                self.root.ids.mrd_escoamento.text=str(mrd)

                try:
                    if float( self.root.ids.mrd_flexao.text ) >= float( self.root.ids.msd.text ):
                        self.root.ids.mrd_flexao.icon_right_color = 0, 255, 0, 1
                    else:
                        self.root.ids.mrd_flexao.icon_right_color = 0, 255, 0, 1
                except:
                    pass
            except:
                pass


            #perfil ze
            #perfil ze
            #perfil ze
            #perfil ze
            #perfil ze
        elif self.root.ids.gerenciador_tabelas.current == "perfilze":
            pass
            # try:
            #     print('flexao ze')
            #
            #     gama = float( self.root.ids.gama_flexao.text )
            #     area = float( self.root.ids.area.text )
            #     moduloe = float( self.root.ids.moduloe.text )
            #     modulog = float( self.root.ids.modulog.text )
            #     fy = float( self.root.ids.fy.text )
            #     cb = float( self.root.ids.cb.text )
            #     ix = float( self.root.ids.ix.text )
            #     iy = float( self.root.ids.iy.text )
            #     wx = float( self.root.ids.wx.text )
            #     wy = float( self.root.ids.wy.text )
            #     iw = float( self.root.ids.iw.text )
            #     it = float( self.root.ids.it.text )
            #     kx = float( self.root.ids.kx.text )
            #     ky = float( self.root.ids.ky.text )
            #     kz = float( self.root.ids.kz.text )
            #     lx = float( self.root.ids.lx.text )
            #     ly = float( self.root.ids.ly.text )
            #     lz = float( self.root.ids.lz.text )
            #     x0 = float( self.root.ids.x0.text )
            #     y0 = float( self.root.ids.y0.text )
            #     rx = float( self.root.ids.rx.text )
            #     ry = float( self.root.ids.ry.text )
            #     r0 = (rx ** 2 + ry ** 2 + x0 ** 2 + y0 ** 2) ** 0.5  # Verificar se é melhor colocar o valor da tabela
            #     bf = float( self.root.ids.bf.text )
            #     bw = float( self.root.ids.bw.text )
            #     t = float( self.root.ids.t.text )
            #     d = float( self.root.ids.d.text )
            #     ri = 0
            #     if t <= 0.63:
            #         ri = t
            #     else:
            #         ri = 1.5 * t
            #     # início do escoamento
            #
            #     # ----larguras efetivas
            #     # Enrijecedor
            #     b_enrijecedor = d - t - ri
            #     teste = b_enrijecedor / t
            #     sigma1 = (bw / 2 - t - ri) * fy / (bw / 2)
            #     sigma2 = (bw / 2 - d) * fy / (bw / 2)
            #     sigma3 = (sigma1 + sigma2) / 2
            #     psi_enrijecedor = (sigma2 / sigma1)  # elemento comprimido com compressão variável
            #     k_enrijecedor = 0.578 / (psi_enrijecedor + 0.34)
            #     ier_enrijecedor = (b_enrijecedor / t) / (0.95 * (k_enrijecedor * moduloe / sigma1) ** 0.5)
            #     bef_enrijecedor = 0
            #     if ier_enrijecedor <= 0.673:
            #         bef_enrijecedor = b_enrijecedor
            #     elif ier_enrijecedor > 0.673:
            #         bef_enrijecedor = b_enrijecedor * (1 - (0.22 / ier_enrijecedor)) / (ier_enrijecedor)
            #     # área retirada do perfil
            #     lret_enrijecedor = b_enrijecedor - bef_enrijecedor
            #     aret_enrijecedor = lret_enrijecedor * t
            #     aef = area - aret_enrijecedor
            #
            #     # momento de inércia da parte a retirar
            #     ixret_enrijecedor = (t * lret_enrijecedor ** 3) / 12 + aret_enrijecedor * (
            #         bw / 2 - t - ri - lret_enrijecedor / 2) ** 2
            #     y_enrijecedor = aret_enrijecedor / aef * (bw / 2 - t - ri - lret_enrijecedor / 2)
            #     yg = bw / 2 + y_enrijecedor
            #
            #     # Mesa
            #     b_mesa = bf - 2 * t - 2 * ri
            #     bef_mesa = 0
            #     ier_mesa = (b_mesa / t) / (0.623 * (moduloe / fy) ** 0.5)
            #     iis = 0
            #     iia = 0
            #     if ier_mesa <= 0.673:
            #         bef_mesa = b_mesa
            #     elif ier_mesa > 0.673:
            #         iis = (t * bef_enrijecedor ** 3 * sin( 90 * pi / 180 ) ** 2) / 12
            #         iia1 = 399 * t ** 4 * (0.487 * ier_mesa - 0.328) ** 3
            #         iia2 = t ** 4 * (56 * ier_mesa + 5)
            #         if iia1 <= iia2:
            #             iia = iia1
            #         else:
            #             iia = iia2
            #         # determinando do valor de n
            #         nlista = [(0.582 - 0.122 * ier_mesa), 1 / 3]
            #         nlista.sort()
            #         n = nlista[1]
            #         k_mesa = 0
            #         if d / b_mesa <= 0.25:
            #             k_mesalista = [(3.57 * (iis / iia) ** n) + 0.43, 4]
            #             k_mesalista.sort()
            #             k_mesa = k_mesalista[0]
            #         elif d / b_mesa > 0.25 and d / b_mesa <= 0.8:
            #             k_mesalista = [((iis / iia) ** n * (4.82 - 5 * d / b_mesa) + 0.43), 4]
            #             k_mesalista.sort()
            #             k_mesa = k_mesalista[0]
            #         ier_mesa2 = ((b_mesa / t) / (0.95 * (k_mesa * moduloe / fy) ** 0.5))
            #         if ier_mesa2 <= 0.673:
            #             bef_mesa = b_mesa
            #         elif ier_mesa2 > 0.673:
            #             bef_mesa = (b_mesa * (1 - (0.22 / ier_mesa2))) / ier_mesa2
            #
            #     # área retirada do perfil
            #     lret_mesa = b_mesa - bef_mesa
            #     aret_mesa = lret_mesa * t
            #     aef = aef - aret_mesa
            #
            #     # momento de inércia do trecho retirado
            #     ixret_mesa = (lret_mesa * t ** 3) / 12 + aret_mesa * (bw / 2 - t / 2) ** 2
            #     # rebaixo do baricentro devido à retirada da mesa
            #
            #     yret_mesa = aret_mesa / aef * (bw / 2 - t / 2)
            #     yg = yg + yret_mesa
            #
            #     # alma
            #     b_alma = bw - 2 * t - 2 * ri
            #     teste_alma = b_alma / t
            #     sigma1_alma = (yg - t - ri) * fy / yg
            #     sigma2_alma = (bw - yg - t - ri) * fy / yg
            #     psi_alma = sigma2_alma / sigma1_alma * (-1)
            #     # coeficiente de flmabagem
            #
            #     k_alma = 4 + 2 * (1 - psi_alma) ** 3 + 2 * (1 - psi_alma)
            #     # índice de esbeltez do elemento
            #     ier_alma = (b_alma / t) / (0.95 * (k_alma * moduloe / sigma1) ** 0.5)
            #     bef_alma = 0
            #     if ier_alma <= 0.673:
            #         bef_alma = b_alma
            #     elif ier_alma > 0.673:
            #         bef_alma = (b_alma * (1 - (0.22 / ier_alma))) / ier_alma
            #
            #     lret_alma = b_alma - bef_alma
            #     aret_alma = lret_alma * t
            #     aef = aef - aret_alma
            #
            #     # momento de inércia da parte a retirar
            #     ixret_alma = (t * lret_alma ** 3) / 12 + aret_alma * (bw / 2 - t - ri - lret_alma / 2) ** 2
            #     y_alma = aret_alma / aef * (bw / 2 - t - ri - lret_alma / 2)
            #     yg = yg + y_alma
            #     ixef = ix - ixret_enrijecedor - ixret_mesa - ixret_alma
            #     # translação do momento de inércia em relação ao eixo que passa pelo CG da seção original para o eixo que passa pelo CG da seção efetiva
            #     ixg = ixef - aef * (yg - bw / 2) ** 2
            #     wef = ixg / yg
            #
            #     # Momento resistente ao escoamento
            #     mrd = wef * fy / gama
            #
            #     # print("enrijecedor",sigma1,sigma2,sigma3,k_enrijecedor,ier_enrijecedor, aret_enrijecedor,ixret_enrijecedor)
            #     # print("mesa",b_mesa, ier_mesa,iia,iis, ier_mesa2,k_mesa,bef_mesa,lret_mesa,aret_mesa, ixret_mesa)
            #     # print('alma', b_alma, ier_alma,k_alma,bef_alma,lret_alma,aret_alma,ixret_alma)
            #     # print(mrd)
            #
            #     """----------------------------------------------------------------------------------------------------------------"""
            #     # Estado limite de instabilidade lateral com torção
            #     ney = (pi ** 2 * moduloe * iy) / (ky * ly) ** 2
            #     nez = (1 / (r0 ** 2)) * ((pi ** 2 * moduloe * iw) / (kz * lz) ** 2 + (modulog * it))
            #     me = 0.5*cb * r0 * (ney * nez) ** 0.5
            #     ier_instabilidade_torcao = (wx * fy / me) ** 0.5
            #     fator_flt = 0
            #     if ier_instabilidade_torcao <= 0.6:
            #         fator_flt = 1
            #     elif ier_instabilidade_torcao > 0.6 and ier_instabilidade_torcao < 1.336:
            #         fator_flt = 1.11 * (1 - 0.278 * ier_instabilidade_torcao ** 2)
            #     elif ier_instabilidade_torcao >= 1.336:
            #         fator_flt = 1 / (ier_instabilidade_torcao ** 2)
            #     # cálculo das larguras efetivas ma tensão Xflt*fy
            #     sigma_flt = fator_flt * fy
            #     # enrijecedor de borda
            #     sigma1_flt_enrijecedor = (bw / 2 - t - ri) * (sigma_flt) / (bw / 2)
            #     sigma2_flt_enrijecedor = (bw / 2 - d) * sigma_flt / (bw / 2)
            #     sigma3_flt_enrijecedor = (sigma1_flt_enrijecedor + sigma2_flt_enrijecedor) / 2
            #     psi_flt_enrijecedor = sigma2_flt_enrijecedor / sigma1_flt_enrijecedor
            #     """O elemento está comprimido com tensões variáveis"""
            #     k_flt_enrijecedor = 0.578 / (psi_flt_enrijecedor + 0.34)
            #     ier_flt_enrijecedor = (b_enrijecedor / t) / (
            #         0.95 * (k_flt_enrijecedor * moduloe / sigma1_flt_enrijecedor) ** 0.5)
            #     bef_flt_enrijecedor = 0
            #     if ier_flt_enrijecedor <= 0.673:
            #         bef_flt_enrijecedor = b_enrijecedor
            #     elif ier_flt_enrijecedor > 0.673:
            #         bef_flt_enrijecedor = b_enrijecedor * (1 - (0.22 / ier_flt_enrijecedor)) / (ier_flt_enrijecedor)
            #
            #         # área retirada do perfil
            #     lret_flt_enrijecedor = b_enrijecedor - bef_flt_enrijecedor
            #     aret_flt_enrijecedor = lret_flt_enrijecedor * t
            #     aef_flt = area - aret_flt_enrijecedor
            #     # momento de inpercia da parte a retirar
            #     ixret_flt_enrijecedor = (t * lret_flt_enrijecedor ** 3) / 12 + aret_flt_enrijecedor * (
            #         bw / 2 - t - ri - lret_flt_enrijecedor / 2) ** 2
            #     # Rebaixo do baricentro
            #     y_flt_enrijecedor = aret_flt_enrijecedor / aef_flt * (bw / 2 - t - ri - lret_flt_enrijecedor / 2)
            #     yg_flt = bw / 2 + y_flt_enrijecedor
            #
            #     # mesa comprimida
            #     ier_flt_mesa = (b_mesa / t) / (0.623 * (moduloe / sigma_flt) ** 0.5)
            #     bef_flt_mesa = 0
            #     is_flt = 0
            #     ia_flt = 0
            #     if ier_flt_mesa <= 0.673:
            #         bef_flt_mesa = b_mesa
            #     elif ier_flt_mesa > 0.673:
            #         is_flt = (t * bef_flt_enrijecedor ** 3 * sin( 90 * pi / 180 ) ** 2) / 12
            #         ia_flt_list = [399 * t ** 4 * (0.487 * ier_flt_mesa - 0.328) ** 3, t ** 4 * (56 * ier_mesa + 5)]
            #         ia_flt_list.sort()
            #         ia_flt = ia_flt_list[0]
            #         # determinqando o valor de n
            #         n_flt_lista = [(0.582 - 0.122 * ier_flt_mesa), 1 / 3]
            #         n_flt_lista.sort()
            #         n_flt = n_flt_lista[1]
            #         k_flt_mesa = 0
            #         if d / b_mesa <= 0.25:
            #             k_flt_mesa_lista = [(3.57 * (is_flt / ia_flt) ** n_flt) + 0.43, 4]
            #             k_flt_mesa_lista.sort()
            #             k_flt_mesa = k_flt_mesa_lista[0]
            #         elif d / b_mesa > 0.25 and d / b_mesa <= 0.8:
            #             k_flt_mesa_lista = [((is_flt / ia_flt) ** n_flt * (4.82 - 5 * d / b_mesa) + 0.43), 4]
            #             k_flt_mesa_lista.sort()
            #             k_flt_mesa = k_flt_mesa_lista[0]
            #         ier_flt_mesa2 = ((b_mesa / t) / (0.95 * (k_flt_mesa * moduloe / sigma_flt) ** 0.5))
            #         if ier_flt_mesa2 <= 0.673:
            #             bef_flt_mesa = b_mesa
            #         elif ier_flt_mesa2 > 0.673:
            #             bef_flt_mesa = (b_mesa * (1 - (0.22 / ier_flt_mesa2))) / ier_flt_mesa2
            #
            #     # área retirada do perfil
            #     lret_flt_mesa = b_mesa - bef_flt_mesa
            #     aret_flt_mesa = lret_flt_mesa * t
            #     aef_flt = aef_flt - aret_flt_mesa
            #     # Momento de inécia do trecho retirado
            #     ixret_flt_mesa = (lret_flt_mesa * t ** 3) / 12 + aret_flt_mesa * (bw / 2 - t / 2) ** 2
            #     # rebaixo do  baricentro
            #     y_flt_mesa = aret_flt_mesa / aef_flt * (bw / 2 - t / 2)
            #     yg_flt = yg_flt + y_flt_mesa
            #
            #     # alma
            #     teste_flt_alma = b_alma / t
            #     sigma1_flt_alma = sigma_flt * (yg_flt - t - ri) / yg_flt
            #     sigma2_flt_alma = sigma_flt * (bw - yg_flt - t - ri) / yg_flt
            #     psi_flt_alma = sigma2_flt_alma / sigma1_flt_alma * (-1)
            #     k_flt_alma = 4 + 2 * (1 - psi_flt_alma) ** 3 + 2 * (1 - psi_flt_alma)
            #     ier_flt_alma = (b_alma / t) / (0.95 * (k_flt_alma * moduloe / sigma1_flt_alma) ** 0.5)
            #     bef_flt_alma = 0
            #     if ier_flt_alma <= 0.673:
            #         bef_flt_alma = b_alma
            #     elif ier_flt_alma > 0.673:
            #         bef_flt_alma = (b_alma * (1 - (0.22 / ier_flt_alma))) / ier_flt_alma
            #
            #     # área retirada da alma
            #     lret_flt_alma = b_alma - bef_flt_alma
            #     aret_flt_alma = lret_flt_alma * t
            #     aef_flt = aef_flt - aret_flt_alma
            #
            #     # momento de inércia da parte a retirar
            #     bef1_flt_alma = 0
            #     bef2_flt_alma = 0
            #     if psi_flt_alma > (-0.236) and psi_flt_alma < 0:
            #         bef1_flt_alma = bef_flt_alma / (3 - psi_flt_alma)
            #         bef2_flt_alma = bef_flt_alma - bef1_flt_alma
            #     elif psi_flt_alma <= (-0.236):
            #         bef1_flt_alma = bef_flt_alma / (3 - psi_flt_alma)
            #         bef2_flt_alma = 0.5 * bef_flt_alma
            #
            #     ixret_flt_alma = (t * lret_flt_alma ** 3) / 12 + aret_flt_alma * (
            #         yg_flt - t - ri - bef1_flt_alma - lret_alma / 2) ** 2
            #     # rebaixo do baricentro
            #     y_flt_alma = aret_flt_alma / aef_flt * (yg_flt - t - ri - lret_flt_alma / 2)
            #     yg_flt = yg_flt + y_flt_alma
            #     ixef_flt = ix - ixret_flt_enrijecedor - ixret_flt_mesa - ixret_flt_alma
            #     # translação do momento de inércia em relação ao eixo que passa pelo cg
            #     ixg_flt = ixef_flt - aef_flt * (yg_flt - bw / 2) ** 2
            #     wcef = ixg_flt / yg_flt
            #
            #     # Momento resistente à instabilidade por torção
            #     mrd_flt = sigma_flt * wcef / gama
            #     # print( is_flt, ia_flt, bef_flt_mesa, mrd, mrd_flt )
            #     print(mrd, mrd_flt)
            #     print('final flexao perfil ze')
            #     mrd_resultado_lista = [mrd, mrd_flt]
            #     mrd_resultado_lista.sort()
            #     mrd_resultado = mrd_resultado_lista[0]
            #     mrd_resultado = float( format( mrd_resultado, '.4f' ) )
            #     self.root.ids.mrd_flexao.text = str( mrd_resultado )
            #     self.root.ids.mrd_escoamento.text=str(mrd)
            #
            #     try:
            #         if float( self.root.ids.mrd_flexao.text ) >= float( self.root.ids.msd.text ):
            #             self.root.ids.mrd_flexao.icon_right_color = 0, 255, 0, 1
            #         else:
            #             self.root.ids.mrd_flexao.icon_right_color = 0, 255, 0, 1
            #     except:
            #         pass
            # except:
            #     pass

    def limite_esbeltez(self):
        try:
            ix = float( self.root.ids.ix.text )
            area = float( self.root.ids.area.text )
            kx = float( self.root.ids.kx.text )
            lx = float( self.root.ids.lx.text )
            raio_giracao= (ix/area)**0.5
            esbeltez = (kx*lx)/raio_giracao

            if esbeltez <= 200:
                self.root.ids.limite_compressao.text='Ok'
                self.root.ids.limite_compressao.icon_right_color = 0, 255, 0, 1
            else:
                self.root.ids.limite_compressao.text = 'Excedido'
                self.root.ids.limite_compressao.icon_right_color = 255, 0, 0, 1

            if esbeltez <= 300:
                self.root.ids.limite_tracao.text='Ok'
                self.root.ids.limite_tracao.icon_right_color = 0, 255, 0, 1
            else:
                self.root.ids.limite_tracao.text = 'Excedido'
                self.root.ids.limite_tracao.icon_right_color = 255, 0, 0, 1
        except:
            pass

    def esforcos_compostos(self):
        try:

            mrd =float(self.root.ids.mrd_escoamento.text)
            msd = float(self.root.ids.msd.text)
            mrd_calc=float(self.root.ids.mrd_flexao.text)
            vrd = float(self.root.ids.cortante.text)
            vsd = float(self.root.ids.vsd.text)
            nsd = float(self.root.ids.nsd.text)
            nrd=0

            #Fletor e Cortante
            if((msd / mrd)**2 + (vsd/vrd)**2)<=1.0:
                self.root.ids.flexao_cortante.text='Ok'
                self.root.ids.flexao_cortante.icon_right_color = 0, 255, 0, 1
            else:
                self.root.ids.flexao_cortante.text='Excedido'
                self.root.ids.flexao_cortante.icon_right_color = 255, 0, 0, 1

            #floetor e carga axial

            if nsd >=0:
                nrd = float(self.root.ids.nrd_tracao.text)
            else:
                nrd = float(self.root.ids.nrd_compressao.text)
                nsd = nsd*(-1)

            if (nsd/nrd + msd/mrd_calc)<=1:
                self.root.ids.flexao_axial.text='Ok'
                self.root.ids.flexao_axial.icon_right_color = 0, 255, 0, 1
            else:
                self.root.ids.flexao_axial.text='Excedido'
                self.root.ids.flexao_axial.icon_right_color = 255, 0, 0, 1
        except:
            pass
    def distorcional_compressao(self):
        try:
            if self.root.ids.gerenciador_tabelas.current=="perfilue" or self.root.ids.gerenciador_tabelas.current=="perfilze":
                t = float( self.root.ids.t.text)
                bw = float( self.root.ids.bw.text)
                bf = float( self.root.ids.bf.text)
                d = float(self.root.ids.d.text)
                pos_hor=0
                pos_ver=0
                ant_hor=0
                ant_ver=0
                listabt = [250,200,125,100,50]
                listabb = [0.4,0.6,0.8,1,1.2,1.4,1.6,1.8,2]
                listabt_invertida=listabt[::-1]
                listabb_invertida=listabb[::-1]
                relacaobb=bf/bw
                relacaobt=bw/t

                tabela_compressao=pd.DataFrame([[0.02, 0.03, 0.04, 0.04, 0.08],[0.03, 0.04, 0.06, 0.06, 0.15],
                                                [0.05, 0.06, 0.08, 0.1, 0.22],[0.06, 0.07, 0.1, 0.12, 0.27],
                                                [0.06,0.07,0.12,0.15,0.27],[0.06,0.08,0.12,0.15,0.27],[0.07,0.08,0.12,0.15,0.27],
                                                [0.07,0.08,0.12,0.15,0.27],[0.07,0.08,0.12,0.15,0.27]])
                tabela_compressao.index=listabb
                tabela_compressao.columns=listabt

                if relacaobt not in listabt and relacaobb not in listabb and relacaobt> 50 and relacaobt <250 \
                    and relacaobb>0.4 and relacaobb<2:

                    for i in listabt:
                        if relacaobt < i:
                            ant_hor = i
                    for i in listabt_invertida:
                        if relacaobt > i:
                            pos_hor = i

                    for i in listabb_invertida:
                        if relacaobb < i:
                            pos_ver = i
                        if relacaobb > i:
                            ant_ver = i
                    y01=tabela_compressao.loc[ant_ver,ant_hor]
                    y11=tabela_compressao.loc[ant_ver,pos_hor]
                    x1= relacaobt
                    x01=ant_hor
                    x11=pos_hor

                    y1=y01+(y11-y01)*(x1-x01)/(x11-x01)


                    y02=tabela_compressao.loc[pos_ver,ant_hor]
                    y12=tabela_compressao.loc[pos_ver,pos_hor]
                    x2=relacaobt
                    x02=ant_hor
                    x12=pos_hor

                    y2 = y02 + (y12 - y02) * (x2 - x02) / (x12 - x02)


                    y03=y1
                    y13=y2
                    x3=relacaobb
                    x03=ant_ver
                    x13=pos_ver

                    y3 = y03 + (y13 - y03) * (x3 - x03) / (x13 - x03)



                elif relacaobt not in listabt and relacaobt>50 and relacaobt<250 and relacaobb in listabb:
                    for i in listabt:
                        if relacaobt < i:
                            ant_hor = i
                    for i in listabt_invertida:
                        if relacaobt > i:
                            pos_hor = i

                    y03=tabela_compressao.loc[relacaobb,ant_hor]
                    y13=tabela_compressao.loc[relacaobb,pos_hor]
                    x3=relacaobt
                    x03=ant_hor
                    x13=pos_hor

                    y3 = y03 + (y13 - y03) * (x3 - x03) / (x13 - x03)

                elif relacaobb not in listabb and relacaobb>0.4 and relacaobb<2 and relacaobt in listabt:
                    for i in listabb_invertida:
                        if relacaobb < i:
                            pos_ver = i
                        if relacaobb > i:
                            ant_ver = i
                    y03=tabela_compressao.loc[ant_ver,relacaobt]
                    y13=tabela_compressao.loc[pos_ver,relacaobt]
                    x3=relacaobb
                    x03=ant_ver
                    x13=pos_ver
                    y3 = y03 + (y13 - y03) * (x3 - x03) / (x13 - x03)


                elif relacaobb in listabb and relacaobt in listabt:
                    y3=tabela_compressao.loc[relacaobb,relacaobt]

                else:
                    y3=100000000
            else:
                y3=0
                d=1
                bw=1
            if (d/bw)>= y3:
                self.root.ids.distorcional_compressao.text='Análise Dispensada'
                self.root.ids.distorcional_compressao.icon_right_color = 0, 255, 0, 1
            else:
                self.root.ids.distorcional_compressao.text='Análise Necessária'
                self.root.ids.distorcional_compressao.icon_right_color = 255, 0, 0, 1
        except:
            pass
    def distorcional_flexao(self):
        try:
            if self.root.ids.gerenciador_tabelas.current=="perfilue" or self.root.ids.gerenciador_tabelas.current=="perfilze":
                t = float( self.root.ids.t.text)
                bw = float( self.root.ids.bw.text)
                bf = float( self.root.ids.bf.text)
                d = float(self.root.ids.d.text)

                pos_hor=0
                pos_ver=0
                ant_hor=0
                ant_ver=0
                listabt = [250,200,125,100,50]
                listabb = [0.4,0.6,0.8,1,1.2,1.4,1.6,1.8,2]
                listabt_invertida=listabt[::-1]
                listabb_invertida=listabb[::-1]
                relacaobb=bf/bw
                relacaobt=bw/t


                tabela_flexao=pd.DataFrame([[0.05,0.06,0.1,0.12, 0.25],
                                                [0.05,0.06,0.1,0.12,0.25],[0.05,0.06,0.09,0.12,0.22],
                                                [0.05,0.06,0.09,0.11,0.22], [0.05,0.06,0.09,0.11,0.2],
                                                [0.05,0.06,0.09,0.1,0.2], [0.05,0.06,0.09,0.1,0.2],
                                                [0.05,0.06,0.09,0.1,0.19],[0.05,0.06,0.09,0.1,0.19]])

                tabela_flexao.index=listabb
                tabela_flexao.columns=listabt
                y3=0
                if relacaobt not in listabt and relacaobb not in listabb and relacaobt> 50 and relacaobt <250 \
                    and relacaobb>0.4 and relacaobb<2:

                    for i in listabt:
                        if relacaobt < i:
                            ant_hor = i
                    for i in listabt_invertida:
                        if relacaobt > i:
                            pos_hor = i

                    for i in listabb_invertida:
                        if relacaobb < i:
                            pos_ver = i
                        if relacaobb > i:
                            ant_ver = i
                    y01=tabela_flexao.loc[ant_ver,ant_hor]
                    y11=tabela_flexao.loc[ant_ver,pos_hor]
                    x1= relacaobt
                    x01=ant_hor
                    x11=pos_hor

                    y1=y01+(y11-y01)*(x1-x01)/(x11-x01)


                    y02=tabela_flexao.loc[pos_ver,ant_hor]
                    y12=tabela_flexao.loc[pos_ver,pos_hor]
                    x2=relacaobt
                    x02=ant_hor
                    x12=pos_hor

                    y2 = y02 + (y12 - y02) * (x2 - x02) / (x12 - x02)


                    y03=y1
                    y13=y2
                    x3=relacaobb
                    x03=ant_ver
                    x13=pos_ver

                    y3 = y03 + (y13 - y03) * (x3 - x03) / (x13 - x03)



                elif relacaobt not in listabt and relacaobt>50 and relacaobt<250 and relacaobb in listabb:
                    for i in listabt:
                        if relacaobt < i:
                            ant_hor = i
                    for i in listabt_invertida:
                        if relacaobt > i:
                            pos_hor = i

                    y03=tabela_flexao.loc[relacaobb,ant_hor]
                    y13=tabela_flexao.loc[relacaobb,pos_hor]
                    x3=relacaobt
                    x03=ant_hor
                    x13=pos_hor

                    y3 = y03 + (y13 - y03) * (x3 - x03) / (x13 - x03)

                elif relacaobb not in listabb and relacaobb>0.4 and relacaobb<2 and relacaobt in listabt:
                    for i in listabb_invertida:
                        if relacaobb < i:
                            pos_ver = i
                        if relacaobb > i:
                            ant_ver = i
                    y03=tabela_flexao.loc[ant_ver,relacaobt]
                    y13=tabela_flexao.loc[pos_ver,relacaobt]
                    x3=relacaobb
                    x03=ant_ver
                    x13=pos_ver
                    y3 = y03 + (y13 - y03) * (x3 - x03) / (x13 - x03)


                elif relacaobb in listabb and relacaobt in listabt:
                    y3=tabela_flexao.loc[relacaobb,relacaobt]

                else:
                    y3=100000000
            else:
                d=1
                bw=1
                y3=0
            if (d/bw)>= y3:
                self.root.ids.distorcional_flexao.text='Análise Dispensada'
                self.root.ids.distorcional_flexao.icon_right_color = 0, 255, 0, 1
            else:
                self.root.ids.distorcional_flexao.text='Análise Necessária'
                self.root.ids.distorcional_flexao.icon_right_color = 255, 0, 0, 1
        except:
            pass
MainApp().run()