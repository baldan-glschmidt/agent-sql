# R126SSV

## Descrição

Solicitação de abertura de vaga - Substituídos

---

## Resumo

- Campos: 4
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSVa | Number(009,0) | Não | Código da solicitação de vaga |
| NumEmp | Number(004,0) | Não | Empresa Requisitante |
| TipCol | Number(001,0) | Não | Tipo de Colaborador Substituído |
| NumCad | Number(009,0) | Não | Cadastro Colaborador Substituído |

---

## Chave Primária

- CodSVa
- NumEmp
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R126SSV_000

**Tabela:** R126SVA

| Origem | Destino |
|--------|---------|
| CodSVa | CodSVa |

