# R088ABA

## Descrição

Abastecimentos do Veículo

---

## Resumo

- Campos: 10
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PlaVei | String(010) | Não | Placa do Veículo |
| DatAba | Date | Não | Data do Abastecimento |
| HorAba | Number(005,0) | Não | Hora Abastecimento |
| QuiAba | Number(007,0) | Sim | Quilometragem no momento do  Abastecimento |
| QuiAnt | Number(007,0) | Sim | Quilometragem anterior no momento do abastecimento |
| CodOem | Number(008,0) | Sim | Código do Fornecedor |
| NumNFS | String(044) | Sim | Número da Nota Fiscal |
| QtdAba | Number(007,3) | Sim | Quantidade de litros Abastecidos |
| ValAba | Number(011,2) | Sim | Valor Total do Abastecimento |
| ValLit | Number(012,3) | Sim | Valor do Litro do Combustível |

---

## Chave Primária

- PlaVei
- DatAba
- HorAba

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R088ABA_000

**Tabela:** R088VEI

| Origem | Destino |
|--------|---------|
| PlaVei | PlaVei |

