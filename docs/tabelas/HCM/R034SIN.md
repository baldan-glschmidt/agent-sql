# R034SIN

## Descrição

Outros Sindicatos do Empregado

---

## Resumo

- Campos: 11
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| CodSin | Number(004,0) | Não | Código do sindicato |
| SocSin | String(001) | Sim | É sócio do sindicato (S,N) |
| PagSin | String(001) | Sim | Contribuição Sindical no Ano |
| TasSin | String(001) | Sim | Paga taxa assistencial (S,N) |
| CusSin | String(001) | Sim | Paga taxa de custeio (S,N) |
| RevSin | String(001) | Sim | Paga Reversão Salarial (S,N) |
| DatIni | Date | Não | Data Início |
| DatFim | Date | Sim | Data Fim |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodSin
- DatIni

---

## Índices

### R034SINIndice2

**Tipo:** Não unico

Campos:
- CodSin

---

## Relacionamentos

### IR_R034SIN_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R034SIN_003

**Tabela:** R014SIN

| Origem | Destino |
|--------|---------|
| CodSin | CodSin |

