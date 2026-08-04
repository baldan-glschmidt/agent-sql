# E069CNP

## Descrição

Cadastros - Convênios - Períodos de Crédito

---

## Resumo

- Campos: 12
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCnv | Number(004,0) | Não | Código do convênio |
| CptCnv | Date | Não | Mês e ano de competência do convênio |
| SeqCnv | Number(008,0) | Não | Sequencial |
| LimCnv | Number(015,2) | Sim | Limite do valor em aberto dos títulos dos clientes ligados ao convênio |
| VlrUti | Number(015,2) | Sim | Valor já utilizado do convênio na competência |
| IndFat | String(001) | Sim | Indicativo se competência já foi faturada |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAtu | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAtu | Date | Sim | Data da última alteração do registro |
| HorAtu | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- CodCnv
- CptCnv
- SeqCnv

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E069CNP_000

**Tabela:** E069CNV

| Origem | Destino |
|--------|---------|
| CodCnv | CodCnv |

