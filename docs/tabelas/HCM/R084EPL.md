# R084EPL

## Descrição

Etapas do Plano de Ação

---

## Resumo

- Campos: 13
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodPln | Number(009,0) | Não | Código do Plano de Ação |
| SeqEtp | Number(003,0) | Não | Sequência Etapa |
| DatIni | Date | Sim | Data Início da Etapa |
| DatFim | Date | Sim | Data Fim da Etapa |
| SitEtp | Number(001,0) | Sim | Situação da Etapa |
| ObsEtp | String(100) | Sim | Observação da Etapa |
| EmpExe | Number(004,0) | Não | Empresa do Colaborador Executor |
| TipCol | Number(001,0) | Sim | Tipo Colabolador Executor |
| NumCad | Number(009,0) | Sim | Cadastro do Colaborador Executor |
| IndEfi | String(001) | Sim | Identificação de eficácia da etapa |
| RecNec | String(250) | Sim | Recursos humanos, administrativos e/ou financeiros necessários para a etapa |
| ConRec | String(250) | Sim | Recursos humanos, administrativos e/ou financeiros necessários para a etapa |

---

## Chave Primária

- NumEmp
- CodPln
- SeqEtp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R084EPL_001

**Tabela:** R084PLN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPln | CodPln |

