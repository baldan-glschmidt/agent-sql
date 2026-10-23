# R088PSE

## Descrição

Parcelas de Seguro de Veículos

---

## Resumo

- Campos: 4
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PlaVei | String(010) | Não | Placa do Veículo |
| DatVen | Date | Não | Data de Vencimento da Parcela de Seguro |
| ValSeg | Number(011,2) | Sim | Valor Segurado |
| SitSeg | Number(001,0) | Sim | Situação Seguro |

---

## Chave Primária

- PlaVei
- DatVen

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R088PSE_000

**Tabela:** R088VEI

| Origem | Destino |
|--------|---------|
| PlaVei | PlaVei |

