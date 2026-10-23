# R070PAL

## Descrição

Pendências de atualização de lista

---

## Resumo

- Campos: 7
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPal | Number(009,0) | Não | Código da Pendência |
| CodDsp | Number(009,0) | Sim | Código do Dispositivo |
| TipOpe | String(001) | Sim | Tipo Operação(Insert/Update/Delete) |
| NumFis | Number(012,0) | Sim | Número Físico do Crachá (Número Serial) |
| TecCra | Number(001,0) | Sim | Tecnologia do Crachá |
| IdtPes | String(023) | Não | Identificador da Pessoa |
| Status | String(001) | Sim | Status |

---

## Chave Primária

- CodPal

---

## Índices

### R070PALIndice1

**Tipo:** Não unico

Campos:
- CodDsp
- TipOpe
- NumFis
- TecCra
- IdtPes

---

## Relacionamentos

Nenhum relacionamento cadastrado.
