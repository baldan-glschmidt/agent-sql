# R030NRQ

## Descrição

Filial - Não-retenção adquirente de incidentes sobre a aquisição de produção

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
| CodFil | Number(006,0) | Não | Código da Filial |
| IndAqu | Number(001,0) | Não | Indicativo de aquisição |
| CmpIni | Date | Não | Competência Início |
| CodPro | Number(009,0) | Não | Cód. processo que determina não-retenção pelo adquirente |
| CodSus | Number(014,0) | Sim | Código Suspensão |
| CmpTer | Date | Sim | Competência Término |

---

## Chave Primária

- NumEmp
- CodFil
- IndAqu
- CmpIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R030NRQ_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

