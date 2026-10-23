# R070PAC

## Descrição

Permissão de Área Controlada

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdtPes | String(023) | Não | Identificador da Pessoa |
| CodPrm | Number(005,0) | Não | Código da Permissão de Área Controlada |
| DatIni | Date | Não | Data Inicial da Permissão de Área Controlada |
| HorIni | Number(005,0) | Não | Hora Inicial da Permissão de Área Controlada |
| DatFim | Date | Sim | Data Final da Permissão de Área Controlada |
| HorFim | Number(005,0) | Sim | Hora Final da Permissão de Área Controlada |

---

## Chave Primária

- IdtPes
- CodPrm
- DatIni
- HorIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R070PAC_001

**Tabela:** R058PRM

| Origem | Destino |
|--------|---------|
| CodPrm | CodPrm |

