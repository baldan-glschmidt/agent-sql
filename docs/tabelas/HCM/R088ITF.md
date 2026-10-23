# R088ITF

## Descrição

Ocorrências no Auto de Infrações de Trânsito

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
| DatInf | Date | Não | Data da Infração |
| HorInf | Number(005,0) | Não | Hora da Infração |
| PlaVei | String(010) | Não | Placa do Veículo |
| CodInf | String(005) | Não | Código da Infração de Trânsito |

---

## Chave Primária

- DatInf
- HorInf
- PlaVei
- CodInf

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R088ITF_003

**Tabela:** R088ITR

| Origem | Destino |
|--------|---------|
| CodInf | CodInf |

