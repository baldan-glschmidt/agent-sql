# R110FIC

## Descrição

Ficha Médica

---

## Resumo

- Campos: 26
- Chave Primária: 2 campo(s)
- Índices: 3
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| CodFic | Number(009,0) | Não | Código Ficha Médica |
| TipAtn | Number(001,0) | Sim | Tipo Atendido |
| TipCol | Number(001,0) | Sim | Tipo Colaborador |
| NumCad | Number(009,0) | Sim | Cadastro Colaborador Atendido |
| CodDep | Number(002,0) | Sim | Codigo Dependente Atendido |
| NumCan | Number(007,0) | Sim | Cadastro do Candidato Atendido |
| NomAtn | String(040) | Sim | Nome do Atendido |
| GruSan | String(003) | Sim | Grupo Sanguíneo |
| PesAtn | Number(006,3) | Sim | Peso do Atendido |
| AltAtn | Number(005,2) | Sim | Altura do Atendido |
| TipFis | String(001) | Sim | Tipo Físico |
| ColDoa | String(001) | Sim | Identifica se a pessoa é doadora de sangue |
| UltDoa | Date | Sim | Última Doação |
| AntPes | String(1950) | Sim | Antecedentes Pessoais |
| AntFam | String(1950) | Sim | Antecedentes Familiares |
| AntPro | String(1950) | Sim | Antecedentes Profissionais |
| ObsFic | String(8001) | Sim | Observações Ficha Médica |
| CodUsu | Number(010,0) | Sim | Código do Usuário |
| DefFis | String(001) | Sim | Deficiente Habilitado ou Reabilitado |
| CodDef | Number(002,0) | Sim | Código da Deficiência |
| BenRea | String(001) | Sim | Beneficiário reabilitado(S/N) |
| TemSub | String(001) | Sim | Indica se o paciente possui subnormalidade |
| CotDef | String(001) | Sim | Preenche cota pessoas com deficiência habilitadas ou beneficiários reabilitados |
| CodMae | Number(002,0) | Sim | Código do dependente referente a mãe do colaborador |
| NomMae | String(070) | Sim | Nome da Mãe |

---

## Chave Primária

- NumEmp
- CodFic

---

## Índices

### R110FICIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad
- CodDep

### R110FICIndice3

**Tipo:** Não unico

Campos:
- NumEmp
- NomAtn
- CodFic

### R110FICIndice4

**Tipo:** Não unico

Campos:
- TemSub
- NumEmp
- CodFic

---

## Relacionamentos

### IR_R110FIC_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

