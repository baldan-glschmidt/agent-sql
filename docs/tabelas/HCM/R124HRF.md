# R124HRF

## Descrição

Colaborador - Referências

---

## Resumo

- Campos: 9
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo de Colaborador Candidato |
| NumCad | Number(009,0) | Não | Cadastro de Candidato |
| SeqRef | Number(002,0) | Não | Sequência do Registro |
| NomRef | String(030) | Sim | Nome da Pessoa Referência |
| NumTel | String(020) | Sim | Telefone de Contato |
| CodRlc | Number(003,0) | Sim | Tipo de Referência |
| DddTel | Number(003,0) | Sim | Código DDD do telefone |
| DdiTel | Number(003,0) | Sim | Código DDI do telefone |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- SeqRef

---

## Índices

### R124HRFIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad
- CodRlc

---

## Relacionamentos

### IR_R124HRF_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R124HRF_006

**Tabela:** R114RLC

| Origem | Destino |
|--------|---------|
| CodRlc | CodRlc |

