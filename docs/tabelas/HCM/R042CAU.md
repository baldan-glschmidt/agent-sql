# R042CAU

## Descrição

Causas de Demissão

---

## Resumo

- Campos: 44
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CauDem | Number(002,0) | Não | Causa Demissão |
| DesDem | String(030) | Sim | Descrição da Causa de Demissão |
| CauRai | Number(002,0) | Sim | Causa do desligamento/transferência p/ Rais |
| ImpCde | String(001) | Sim | Imprimir Comunicado de Dispensa (S,N) |
| TipTsf | String(001) | Sim | Transferência |
| UsaAvi | String(001) | Sim | Data de aviso da rescisão (S,N) |
| IndRcs | String(001) | Sim | Dias indenizados |
| ReaRcs | String(001) | Sim | Dias reavidos |
| FcaRcs | String(001) | Sim | Dias Antecipados (Fim de Contrato Antecipado) |
| AvoFca | String(001) | Sim | Dias Antecipados somam na contagem dos Avos de Férias e 13° Salário. |
| CalPrz | String(001) | Sim | Prazo Determinado (Lei 9.601/98) |
| CodSaq | String(003) | Sim | Código do saque do Fgts |
| CodCag | Number(002,0) | Sim | Código p/ Caged e Comunicado de Dispensa |
| LetFgt | String(001) | Sim | Letra Movto Fgts |
| CheEst | String(001) | Sim | Checar estabilidade (S,N) |
| PagSaf | String(001) | Sim | Paga Salário Família |
| PagFgt | String(001) | Sim | Pagar Fgts na Rescisão |
| PagMul | String(001) | Sim | Pagar Multa Fgts na Rescisão |
| Pag13s | String(001) | Sim | Pagar 13° Salário Proporcional |
| Pag13i | String(001) | Sim | Pagar 13° Salário Indenizado |
| PagFer | String(001) | Sim | Pagar Férias Proporcionais |
| PagGra | String(001) | Sim | Pagar Gratificação |
| PagDis | String(001) | Sim | Indenização Mês Anterior ao Dissídio |
| PagLic | Number(001,0) | Sim | Pagar Licença Especial |
| CntAvi | String(001) | Sim | Contagem dos Dias de Aviso Prévio |
| ConRec | String(001) | Sim | Controlar Recontratação |
| TipNot | Number(003,0) | Sim | Tipo da Anotação |
| OutEve | String(001) | Sim | Calcula Outros Eventos Rescisão |
| PagGrt | String(001) | Sim | Pagar gratificação nas rescisões |
| SitSij | Number(002,0) | Sim | Indica qual é a situação referente ao SIJP |
| AuxEnt | String(001) | Sim | Indica se o motivo pode ser utilizado na entrevista de desligamento |
| DWorkf | String(001) | Sim | Divulga no Workflow |
| DiaBlq | Number(001,0) | Sim | Número de dias, após a data de demissão,  que o crachá será bloqueado |
| HomNet | String(003) | Sim | Código Afastamento HomologNet |
| MosMov | String(001) | Sim | Considerar no Portlet de Movimentações |
| VtrRes | Number(001,0) | Sim | Desconto Vale Transporte |
| AfaDem | String(001) | Sim | Permite afastamento na data de rescisão |
| MotEFD | Number(002,0) | Sim | Motivo Desligamento eSocial |
| ProTra | String(001) | Sim | Habilitar Processo Trabalhista |
| SldMen | Number(001,0) | Sim | Calcular saldo de salário mensalista |
| IniCon | Number(001,0) | Sim | Informar como será o início de contagem da data do pagamento |
| DesFer | Number(001,0) | Sim | Descontar Férias Antecipadas |
| MuQuPr | String(001) | Sim | Pagar Multa Qualificação Profissional |
| IndPdv | String(001) | Sim | Programa de Demissão Voluntária (PDV) |

---

## Chave Primária

- CauDem

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
