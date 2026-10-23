# R008EVC

## Descrição

Eventos

---

## Resumo

- Campos: 41
- Chave Primária: 2 campo(s)
- Índices: 2
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodTab | Number(003,0) | Não | Código da Tabela Eventos |
| CodEve | Number(004,0) | Não | Código do Evento |
| DesEve | String(025) | Sim | Descrição do Evento |
| CrtEve | String(003) | Sim | Característica do Evento |
| CodCrt | Number(004,0) | Sim | Código Interno Característica |
| HorUti | String(001) | Sim | Hora/Dia Útil (S,N) |
| RgrEve | Number(003,0) | Sim | Regra do Evento |
| RgrEsp | Number(003,0) | Sim | Regra Específica do Evento |
| TipEve | Number(001,0) | Sim | Tipo do Evento |
| NatEve | Number(001,0) | Sim | Natureza do Evento |
| SinSel | String(001) | Sim | Sinal da Seleção |
| CodSel | Number(003,0) | Sim | Código de Seleção |
| ValCal | Number(013,4) | Sim | Valor de Cálculo |
| ValTet | Number(011,2) | Sim | Valor do Teto do Cálculo |
| CodClc | Number(004,0) | Sim | Código Lançamento Contábil |
| AlfaEv | String(010) | Sim | Código Alfa do Evento |
| TipInf | String(001) | Sim | Unidade do Evento |
| DimNor | String(001) | Sim | Diminuir das Horas Normais |
| GerEve | Number(001,0) | Sim | Tipo Geração do Evento |
| PrjEve | String(001) | Sim | Projetar o Evento |
| PerEve | String(001) | Sim | Periodicidade dos Limites do Evento |
| CodSin | Number(004,0) | Sim | Código do Sindicato onde o Evento é válido |
| RatEve | String(001) | Sim | Ratear Evento |
| TipRat | Number(001,0) | Sim | Tipo de Rateio |
| RemCag | String(001) | Sim | Remuneração Caged |
| EveDpo | Number(004,0) | Sim | Código do Evento de Diferença Positiva |
| EveDne | Number(004,0) | Sim | Código do Evento de Diferença Negativa |
| ArrVal | Number(001,0) | Sim | Arredondamento |
| ArrPre | Number(002,0) | Sim | Precisão |
| ArrEsp | Number(001,0) | Sim | Especial |
| RemPat | String(001) | Sim | Remuneração PAT Rais |
| RubHom | Number(003,0) | Sim | Rubrica HomologNet |
| ObsEve | String(255) | Sim | Observação sobre o evento |
| IniVal | Date | Sim | Competência Início Validade |
| FimVal | Date | Sim | Competência Final Validade |
| DesCom | String(100) | Sim | Descrição Completa do Evento |
| USU_GrpEvt | Number(002,0) | Sim | Grupo de Eventos |
| USU_Item30 | String(001) | Sim | Item 3.0 Fiesp |
| USU_Item31 | String(001) | Sim | Item 3.1 Fiesp |
| USU_Item40 | String(001) | Sim | USU_Item40 |
| USU_LisRef | String(001) | Sim | Listar Referencia no relatorio do IBGE |

---

## Chave Primária

- CodTab
- CodEve

---

## Índices

### R008EVCIndice2

**Tipo:** Não unico

Campos:
- CodTab
- DesEve

### R008EVCIndice3

**Tipo:** Não unico

Campos:
- RgrEve
- CodTab
- CodEve

---

## Relacionamentos

### IR_R008EVC_000

**Tabela:** R008EVM

| Origem | Destino |
|--------|---------|
| CodTab | CodTab |

