# R088VDA

## Descrição

Dados Complementares da Aquisição e Venda de Veículos

---

## Resumo

- Campos: 16
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PlaVei | String(010) | Não | Placa do Veículo |
| DatCmp | Date | Sim | Data da Compra do Veículo - Evento Compra |
| ValCmp | Number(011,2) | Sim | Valor do Veículo na Compra - Evento Compra |
| ComPra | String(040) | Sim | Comprador do Veículo - Evento Compra |
| DocCmp | String(040) | Sim | Documento Comprador do Veículo - Evento Compra |
| ComVen | String(040) | Sim | Vendedor do Veículo - Evento Compra |
| DocCvp | String(040) | Sim | Documento Vendedor do Veículo - Evento Compra |
| NumNfs | String(044) | Sim | Nota Fiscal - Evento Compra |
| DatNfs | Date | Sim | Data de Emissão da Nota Fiscal - Evento Compra |
| DatVen | Date | Sim | Data da Venda do Veículo - Evento Venda |
| ValVen | Number(011,2) | Sim | Valor do Veículo na Venda - Evento Venda |
| VenDed | String(040) | Sim | Vendedor do Veículo - Evento Venda |
| DocVen | String(040) | Sim | Documento Vendedor do Veículo - Evento Venda |
| VenDcm | String(040) | Sim | Comprador do Veículo - Evento Venda |
| DocVcm | String(040) | Sim | Documento Comprador do Veículo - Evento Venda |
| QuiAqu | Number(007,0) | Sim | Quilometragem quando da aquisição do veículo |

---

## Chave Primária

- PlaVei

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R088VDA_000

**Tabela:** R088VEI

| Origem | Destino |
|--------|---------|
| PlaVei | PlaVei |

