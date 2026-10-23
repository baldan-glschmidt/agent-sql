# R124CAA

## Descrição

Colaborador - Áreas Pretendidas

---

## Resumo

- Campos: 7
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo de Colaborador Candidato |
| NumCad | Number(009,0) | Não | Cadastro do Candidato |
| DatSol | Date | Não | Data da Solicitação |
| CodSol | Number(003,0) | Não | Tipo da Solicitação |
| SeqAre | Number(003,0) | Não | Sequência para permitir determinar prioridade |
| AreAtu | Number(003,0) | Não | Código da área desejada |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatSol
- CodSol
- SeqAre
- AreAtu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R124CAA_004

**Tabela:** R124CSL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| DatSol | DatSol |
| CodSol | CodSol |

### IR_R124CAA_006

**Tabela:** R024AAT

| Origem | Destino |
|--------|---------|
| AreAtu | AreAtu |

