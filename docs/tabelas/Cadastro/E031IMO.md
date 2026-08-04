# E031IMO

## Descrição

Tabelas - Moedas - Índices por Data

---

## Resumo

- Campos: 11
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodMoe | String(003) | Não | Código da moeda ou índice |
| DatMoe | Date | Não | Data da cotação da moeda ou índice |
| VlrCot | Number(019,10) | Sim | Valor da cotação |
| VlrPre | Number(019,10) | Sim | Valor de previsão |
| TxnCom | Number(008,4) | Sim | Taxa de compra do título público |
| TxnVen | Number(008,4) | Sim | Taxa de venda do título público |
| PreUni | Number(015,6) | Sim | Preço unitário do título público |
| IniMda | Number(008,4) | Sim | Intervalo indicativo mínimo D0 (Dia Zero) do título público |
| InaMda | Number(008,4) | Sim | Intervalo indicativo máximo D0 (Dia Zero) do título público |
| IniMdp | Number(008,4) | Sim | Intervalo indicativo mínimo D1 (Dia Um) do título público |
| InaMdp | Number(008,4) | Sim | Intervalo indicativo máximo D1 (Dia Um) do título público |

---

## Chave Primária

- CodMoe
- DatMoe

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E031IMO_000

**Tabela:** E031MOE

| Origem | Destino |
|--------|---------|
| CodMoe | CodMoe |

