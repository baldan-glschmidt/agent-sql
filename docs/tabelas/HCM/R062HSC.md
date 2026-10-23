# R062HSC

## Descrição

Histórico de Status dos Coletores

---

## Resumo

- Campos: 5
- Chave Primária: 0 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodDsp | Number(009,0) | Sim | Código do Dispositivo |
| DspPai | Number(009,0) | Sim | Código do Dispositivo Pai. |
| ModOpe | Number(001,0) | Sim | Modo de Operação do Coletor |
| DatSco | Date | Sim | Data da Mudança do Status |
| HorSco | Number(005,0) | Sim | Hora da Mudança do Status |

---

## Chave Primária

Não possui.

---

## Índices

### R062HSCIndice1

**Tipo:** Não unico

Campos:
- CodDsp
- ModOpe
- HorSco
- DatSco

---

## Relacionamentos

Nenhum relacionamento cadastrado.
