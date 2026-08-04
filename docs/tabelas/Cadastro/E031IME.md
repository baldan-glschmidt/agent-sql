# E031IME

## Descrição

Tabelas - Moedas - Índices por Data (Especial)

---

## Resumo

- Campos: 26
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodMoe | String(003) | Não | Código da moeda ou índice |
| DatMoe | Date | Não | Data da cotação da moeda ou índice |
| VlrC01 | Number(019,10) | Sim | Valor Cotação 1M |
| VlrP01 | Number(019,10) | Sim | Valor Previsão 1M |
| VlrC02 | Number(019,10) | Sim | Valor Cotação 2M |
| VlrP02 | Number(019,10) | Sim | Valor Previsão 2M |
| VlrC03 | Number(019,10) | Sim | Valor Cotação 3M |
| VlrP03 | Number(019,10) | Sim | Valor Previsão 3M |
| VlrC04 | Number(019,10) | Sim | Valor Cotação 4M |
| VlrP04 | Number(019,10) | Sim | Valor Previsão 4M |
| VlrC05 | Number(019,10) | Sim | Valor Cotação 5M |
| VlrP05 | Number(019,10) | Sim | Valor Previsão 5M |
| VlrC06 | Number(019,10) | Sim | Valor Cotação 6M |
| VlrP06 | Number(019,10) | Sim | Valor Previsão 6M |
| VlrC07 | Number(019,10) | Sim | Valor Cotação 7M |
| VlrP07 | Number(019,10) | Sim | Valor Previsão 7M |
| VlrC08 | Number(019,10) | Sim | Valor Cotação 8M |
| VlrP08 | Number(019,10) | Sim | Valor Previsão 8M |
| VlrC09 | Number(019,10) | Sim | Valor Cotação 9M |
| VlrP09 | Number(019,10) | Sim | Valor Previsão 9M |
| VlrC10 | Number(019,10) | Sim | Valor Cotação 10M |
| VlrP10 | Number(019,10) | Sim | Valor Previsão 10M |
| VlrC11 | Number(019,10) | Sim | Valor Cotação 11M |
| VlrP11 | Number(019,10) | Sim | Valor Previsão 11M |
| VlrC12 | Number(019,10) | Sim | Valor Cotação 12M |
| VlrP12 | Number(019,10) | Sim | Valor Previsão 12M |

---

## Chave Primária

- CodMoe
- DatMoe

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E031IME_000

**Tabela:** E031MOE

| Origem | Destino |
|--------|---------|
| CodMoe | CodMoe |

