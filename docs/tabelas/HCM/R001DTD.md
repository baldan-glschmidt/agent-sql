# R001DTD

## Descrição

Períodos de Horas Dispensadas

---

## Resumo

- Campos: 5
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodHDi | Number(003,0) | Não | Código das Horas Dispensadas |
| DInHDi | Date | Não | Data Inicial das Horas Dispensadas |
| HInHDi | Number(005,0) | Não | Hora Inicial das Horas Dispensadas |
| DFiHDi | Date | Sim | Data Final das Horas Dispensadas |
| HFiHDi | Number(005,0) | Sim | Hora Final das Horas Dispensadas |

---

## Chave Primária

- CodHDi
- DInHDi
- HInHDi

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R001DTD_000

**Tabela:** R001HDI

| Origem | Destino |
|--------|---------|
| CodHDi | CodHDi |

