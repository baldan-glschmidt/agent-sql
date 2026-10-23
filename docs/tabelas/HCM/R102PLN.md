# R102PLN

## Descrição

Trabalhos do SESMT - Plano de Ação

---

## Resumo

- Campos: 3
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodTbr | Number(006,0) | Não | Código do Trabalho da Brigada |
| CodPln | Number(009,0) | Não | Código do Plano de Ação |

---

## Chave Primária

- NumEmp
- CodTbr
- CodPln

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R102PLN_001

**Tabela:** R102TBR

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodTbr | CodTbr |

### IR_R102PLN_002

**Tabela:** R084PLN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPln | CodPln |

