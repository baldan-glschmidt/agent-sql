select a.USU_NumSCI as CI,
       a.USU_DatGer as Data_CI,
       a.USU_CodCCU as Centro_Custo,
       b.Nomcom     as Nome_Solicitante,
       a.USU_DesTCI as Objetivo_CI,
       a.USU_DesMCI as Motivo_CI,
       a.usu_vlrliq as Valor,
       a.usu_motexp as Descricao_CI
  from (Select USU_TCICab.USU_NumSCI,
               USU_TCIMot.USU_MotSCI,
               USU_TCIMot.USU_DesMCI,
               USU_TCITip.USU_TipSCI,
               USU_TCITip.USU_DesTCI,
               USU_TCICab.USU_CodSet,
               USU_TCICab.USU_UsuGer,
               USU_TCICadSet.USU_NomSet,
               USU_TCICab.USU_DepAtu,
               USU_TCICab.USU_DepGer,
               USU_TCICadDep.USU_NomDep,
               USU_TCICadUsu.USU_CodUsu,
               R910USU.NomCom,
               USU_TCICab.USU_CodCCU,
               E044CCU.DesCCU,
               USU_TCICab.USU_CodCli,
               E085CLI.NomCli,
               USU_TCICab.USU_CliFin,
               CliFin.NomCli as NomCliFin,
               USU_TCICab.USU_CodFor,
               E095FOR.NomFor,
               USU_TCICab.USU_DatVen,
               --USU_TCICab.USU_VlrLiq,
               NVL((select sum(usu_tcidet.usu_qtdprv * usu_tcidet.usu_vlrliq)
                     from usu_tcidet
                    where usu_tcidet.usu_numsci = USU_TCICab.usu_numsci
                      and usu_tcidet.usu_codemp = USU_TCICab.usu_codemp
                      and usu_tcidet.usu_codfil = USU_TCICab.usu_codfil),
                   USU_TCICab.USU_VlrLiq) as usu_vlrliq,
               USU_TCICab.USU_DatGer,
               USU_TCICab.usu_motexp,
               Case
                 When (Trim(USU_TCICab.USU_VlrLiqMoe) Is Null) Or
                      (USU_TCICab.USU_VlrLiqMoe = '01') Then
                  'R$'
                 Else
                  USU_TCICab.USU_VlrLiqMoe
               End as VlrLiqMoe
          From SAPPROT.USU_TCICab
          Left Join SAPPROT.USU_TCICadUsu
            On USU_TCICadUsu.USU_CodEmp = USU_TCICab.USU_CodEmp
           And USU_TCICadUsu.USU_CodDep = USU_TCICab.USU_DepAtu
           And USU_TCICadUsu.USU_CodSet = USU_TCICab.USU_CodSet
          Left Join SAPPROT.USU_TCICadSet
            On USU_TCICadSet.USU_CodEmp = USU_TCICab.USU_CodEmp
           And USU_TCICadSet.USU_CodSet = USU_TCICab.USU_CodSet
          Left Join SAPPROT.USU_TCICadDep
            On USU_TCICadDep.USU_CodEmp = USU_TCICab.USU_CodEmp
           And USU_TCICadDep.USU_CodSet = USU_TCICab.USU_CodSet
           And USU_TCICadDep.USU_CodDep = USU_TCICab.USU_DepAtu
          Left Join SAPPROT.USU_TCIMot
            On USU_TCIMot.USU_CodEmp = USU_TCICab.USU_CodEmp
           And USU_TCIMot.USU_CodSet = USU_TCICab.USU_CodSet
           And USU_TCIMot.USU_MotSCI = USU_TCICab.USU_MotSCI
          Left Join SAPPROT.USU_TCITip
            On USU_TCITip.USU_CodEmp = USU_TCICab.USU_CodEmp
           And USU_TCITip.USU_CodSet = USU_TCICab.USU_CodSet
           And USU_TCITip.USU_TipSCI = USU_TCICab.USU_TipSCI
          Left Join SAPPROT.E044CCU
            On E044CCU.CodEmp = USU_TCICab.USU_CodEmp
           And E044CCU.CodCCU = USU_TCICab.USU_CodCCU
          Left Join SAPPROT.E085CLI
            On E085CLI.CodCli = USU_TCICab.USU_CodCli
          Left Join SAPPROT.E085CLI CliFin
            On CliFin.CodCli = USU_TCICab.USU_CliFin
          Left Join SAPPROT.E095FOR
            On E095FOR.CodFor = USU_TCICab.USU_CodFor
          Left Join SAPPROT.R910USU
            On R910USU.CodEnt = USU_TCICadUsu.USU_CodUsu
         Where USU_StaSCI = 'ANDAMENTO'
           And USU_TCICadUsu.USU_SitUsu = 'A'
           And USU_TCICadUsu.USU_CodUsu = &CodUsu
         Order By USU_TCICab.USU_NumSCI, R910USU.NomCom) a,
       r910usu b
 where a.usu_usuger = b.codent;
