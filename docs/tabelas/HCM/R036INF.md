# R036INF

## Descrição

Dependentes - Quantidade de dependentes de IRRF e Salário-família

---

## Resumo

- Campos: 7
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Empregado |
| DatAlt | Date | Não | Data da Alteração |
| DepIrf | Number(002,0) | Sim | Número de Dependentes do IR |
| DepSaf | Number(002,0) | Sim | Número de Dependentes do Salário Família |
| GerLei | String(001) | Sim | Indica se o registro foi criado na geração do leiaute do colaborador |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R036INF_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

