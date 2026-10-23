# R600ATU

## Descrição

Pendências de Atualização do Cartão

---

## Resumo

- Campos: 11
- Chave Primária: 1 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdtReg | String(014) | Não | Identificador do Registro de Atualização |
| DatPen | Date | Sim | Data de Envio da Pendência |
| HorPen | Number(005,0) | Sim | Hora de Envio da Pendência |
| StaPen | Number(001,0) | Sim | Tipo de Pendência |
| NumCra | Number(012,0) | Sim | Número do Crachá |
| NumFis | Number(012,0) | Sim | Número Físico do Crachá (Número Serial) |
| CodCon | Number(002,0) | Sim | Código do campo a ser atualizado |
| InfPen | String(056) | Sim | Informação a ser atualizada |
| DatCmd | Date | Sim | Data do Comando Enviado |
| HorCmd | Number(005,0) | Sim | Hora do Comando Enviado |
| RetExe | String(255) | Sim | Retorno da Execução do Comando |

---

## Chave Primária

- IdtReg

---

## Índices

### R600ATUIndice2

**Tipo:** Não unico

Campos:
- DatPen
- HorPen

### R600ATUIndice3

**Tipo:** Não unico

Campos:
- NumCra

---

## Relacionamentos

Nenhum relacionamento cadastrado.
