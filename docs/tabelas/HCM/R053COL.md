# R053COL

## Descrição

RAIS - Registro Colaborador

---

## Resumo

- Campos: 81
- Chave Primária: 8 campo(s)
- Índices: 1
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EmpArq | Number(004,0) | Não | Código da Empresa no Arquivo |
| AnoBas | Number(004,0) | Não | Ano Base da Rais |
| FilArq | Number(006,0) | Não | Código da Filial no Arquivo |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Empregado |
| DatAdm | Date | Não | Data de Admissão |
| CodVin | Number(002,0) | Não | Tipo de Vínculo |
| PreFix | String(002) | Sim | Prefixo do Estabelecimento |
| AnoChe | Number(004,0) | Sim | Ano de Chegada |
| NumCtp | Number(013,0) | Sim | Número da Carteira de Trabalho |
| TipAdm | Number(002,0) | Sim | Tipo de Admissão |
| DatDem | Date | Sim | Data da Demissão |
| CauDem | Number(002,0) | Sim | Causa da Demissão |
| SalEmp | Number(011,2) | Sim | Salário Atual |
| TipSal | Number(001,0) | Sim | Tipo do Salário |
| HorSem | Number(002,0) | Sim | Horas Semanais |
| ValM01 | Number(011,2) | Sim | Valor Salário Janeiro |
| ValM02 | Number(011,2) | Sim | Valor Salário Fevereiro |
| ValM03 | Number(011,2) | Sim | Valor Salário Março |
| ValM04 | Number(011,2) | Sim | Valor Salário Abril |
| ValM05 | Number(011,2) | Sim | Valor Salário Maio |
| ValM06 | Number(011,2) | Sim | Valor Salário Junho |
| ValM07 | Number(011,2) | Sim | Valor Salário Julho |
| ValM08 | Number(011,2) | Sim | Valor Salário Agosto |
| ValM09 | Number(011,2) | Sim | Valor Salário Setembro |
| ValM10 | Number(011,2) | Sim | Valor Salário Outubro |
| ValM11 | Number(011,2) | Sim | Valor Salário Novembro |
| ValM12 | Number(011,2) | Sim | Valor Salário Dezembro |
| Val13A | Number(011,2) | Sim | Valor Adiantamento 13° Salário |
| Mes13A | Number(002,0) | Sim | Mês Adiantamento |
| Val13I | Number(011,2) | Sim | Valor 13° Salário Integral |
| Mes13I | Number(002,0) | Sim | Mês 13° Salário |
| AviPre | Number(011,2) | Sim | Valor Aviso Prévio |
| RacCor | Number(001,0) | Sim | Raça / Cor |
| TipSex | Number(001,0) | Sim | Sexo do Colaborador |
| ColDef | Number(001,0) | Sim | Deficiente Físico Habilitado ou Reabilitado |
| Mot1Af | Number(002,0) | Sim | Motivo Pimeiro Afastamento |
| Ini1Af | Date | Sim | Início Primeiro Afastamento |
| Fim1Af | Date | Sim | Final Primeiro Afastamento |
| Mot2Af | Number(002,0) | Sim | Motivo Segundo Afastamento |
| Ini2Af | Date | Sim | Início Segundo Afastamento |
| Fim2Af | Date | Sim | Final Segundo Afastamento |
| Mot3Af | Number(002,0) | Sim | Motivo Terceiro Afastamento |
| Ini3Af | Date | Sim | Início Terceiro Afastamento |
| Fim3Af | Date | Sim | Final Terceiro Afastamento |
| QtdAfa | Number(003,0) | Sim | Quantidade de Dias Afastados |
| OriMov | String(001) | Sim | Origem do Registro |
| SalPat | Number(011,2) | Sim | Salário PAT |
| LocTra | Number(007,0) | Sim | Município do Local de Trabalho |
| HorM01 | Number(010,0) | Sim | Horas Efetivamente Trabalhadas Janeiro |
| HorM02 | Number(010,0) | Sim | Horas Efetivamente Trabalhadas Fevereiro |
| HorM03 | Number(010,0) | Sim | Horas Efetivamente Trabalhadas Março |
| HorM04 | Number(010,0) | Sim | Horas Efetivamente Trabalhadas Abril |
| HorM05 | Number(010,0) | Sim | Horas Efetivamente Trabalhadas Maio |
| HorM06 | Number(010,0) | Sim | Horas Efetivamente Trabalhadas Junho |
| HorM07 | Number(010,0) | Sim | Horas Efetivamente Trabalhadas Julho |
| HorM08 | Number(010,0) | Sim | Horas Efetivamente Trabalhadas Agosto |
| HorM09 | Number(010,0) | Sim | Horas Efetivamente Trabalhadas Setembro |
| HorM10 | Number(010,0) | Sim | Horas Efetivamente Trabalhadas Outubro |
| HorM11 | Number(010,0) | Sim | Horas Efetivamente Trabalhadas Novembro |
| HorM12 | Number(010,0) | Sim | Horas Efetivamente Trabalhadas Dezembro |
| FerInd | Number(011,2) | Sim | Férias Indenizadas |
| MulRes | Number(011,2) | Sim | Multa Rescisória |
| ValBan | Number(011,2) | Sim | Banco de Horas |
| CmpBan | Number(002,0) | Sim | Quantidade Competências Banco Horas |
| ValDis | Number(011,2) | Sim | Dissídio Coletivo |
| CmpDis | Number(002,0) | Sim | Quantidade Competências Dissídio Coletivo |
| ValGra | Number(011,2) | Sim | Gratificação |
| CmpGra | Number(002,0) | Sim | Quantidade Competências Gratificação |
| ColSin | Number(001,0) | Sim | Indicador de Colaborador Sindicalizado |
| CodCb2 | String(006) | Sim | Cbo 2002 do Cargo |
| BasAu1 | Number(011,2) | Sim | Uso Exclusivo da Senior |
| ValAu1 | Number(011,2) | Sim | Uso Exclusivo da Senior |
| TipAux | Number(005,0) | Sim | Uso Exclusivo da Senior |
| AprGra | Number(001,0) | Sim | Indicador de vínculo de aprendiz grávida |
| TraPar | Number(001,0) | Sim | Indicador de trabalho parcial |
| TelTra | Number(001,0) | Sim | Indicador de teletrabalho |
| TraInt | Number(001,0) | Sim | Indicador de trabalho intermitente |
| MatEso | String(030) | Sim | Matrícula |
| CatEso | Number(004,0) | Sim | Categoria |

---

## Chave Primária

- EmpArq
- AnoBas
- FilArq
- NumEmp
- TipCol
- NumCad
- DatAdm
- CodVin

---

## Índices

### R053COLIndice2

**Tipo:** Não unico

Campos:
- AnoBas
- NumEmp
- TipCol
- NumCad
- OriMov

---

## Relacionamentos

### IR_R053COL_002

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| EmpArq | NumEmp |
| FilArq | CodFil |

### IR_R053COL_003

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R053COL_007

**Tabela:** R022VIN

| Origem | Destino |
|--------|---------|
| CodVin | CodVin |

