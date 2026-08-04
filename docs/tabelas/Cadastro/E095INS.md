# E095INS

## Descrição

Cadastros - Fornecedores - Controle de Retenção de INSS

---

## Resumo

- Campos: 6
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodFor | Number(009,0) | Não | Código do fornecedor |
| MesAno | Date | Não | Mês / Ano da retenção do INSS |
| VlrBit | Number(015,2) | Sim | Valor base do INSS retido por terceiros |
| VlrInt | Number(015,2) | Sim | Valor do INSS retido por terceiros |
| VlrBie | Number(015,2) | Sim | Valor base do INSS retido pela empresa |
| VlrIne | Number(015,2) | Sim | Valor do INSS retido pela empresa |

---

## Chave Primária

- CodFor
- MesAno

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E095INS_000

**Tabela:** E095FOR

| Origem | Destino |
|--------|---------|
| CodFor | CodFor |

