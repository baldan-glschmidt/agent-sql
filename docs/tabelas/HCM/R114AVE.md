# R114AVE

## Descrição

Etapas Recrutamento/Seleção - Avaliadores

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
| CodEta | Number(003,0) | Não | Código Etapa |
| NumEmp | Number(004,0) | Não | Código da Empresa do Avaliador |
| TipCol | Number(001,0) | Não | Tipo de Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Avaliador |

---

## Chave Primária

- CodEta
- NumEmp
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R114AVE_000

**Tabela:** R114ETA

| Origem | Destino |
|--------|---------|
| CodEta | CodEta |

