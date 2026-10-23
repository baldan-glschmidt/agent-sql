# R086ICO

## Descrição

Investigação Ocorrência - Comissão/Membros

---

## Resumo

- Campos: 8
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
| SeqMeb | Number(002,0) | Não | Sequência da Testemunha |
| TipMeb | Number(001,0) | Sim | Origem do Membro |
| EmpMeb | Number(004,0) | Sim | Código da Empresa |
| TipCol | Number(001,0) | Sim | Tipo Colaborador |
| CadMeb | Number(009,0) | Sim | Cadastro do Colaborador |

---

## Chave Primária

- NumEmp
- TipOco
- CodInv
- SeqMeb

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R086ICO_002

**Tabela:** R086INV

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipOco | TipOco |
| CodInv | CodInv |

