# R086ITE

## Descrição

Investigação Ocorrência - Testemunhas

---

## Resumo

- Campos: 9
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipOco | Number(001,0) | Não | Tipo da Ocorrência (Acidente/Incidente) |
| CodInv | Number(006,0) | Não | Código da Investigação |
| SeqTes | Number(002,0) | Não | Sequência da Testemunha |
| EmpTes | Number(004,0) | Sim | Código da Empresa |
| TipTes | Number(001,0) | Sim | Tipo Colaborador |
| CadTes | Number(009,0) | Sim | Cadastro do Colaborador |
| NomTes | String(040) | Sim | Nome Testemunha |
| DepTes | String(2000) | Sim | Depoimento da Testemunha |

---

## Chave Primária

- NumEmp
- TipOco
- CodInv
- SeqTes

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R086ITE_002

**Tabela:** R086INV

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipOco | TipOco |
| CodInv | CodInv |

