# R088CON

## Descrição

Controle de Veículos

---

## Resumo

- Campos: 9
- Chave Primária: 4 campo(s)
- Índices: 4
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdtPes | String(023) | Não | Identificador da Pessoa |
| NumFis | Number(012,0) | Não | Número Físico do Crachá |
| TecCra | Number(001,0) | Não | Tecnologia do Crachá |
| PlaVei | String(010) | Não | Placa do Veículo |
| CraVei | Number(012,0) | Sim | Crachá do Veículo |
| DatVal | String(016) | Sim | Data de Validade do Crachá |
| SitCra | Number(002,0) | Sim | Situação do Crachá |
| ConLPR | String(001) | Sim | Participa do Controle LPR |
| VeiFro | String(001) | Sim | Veículo da Frota |

---

## Chave Primária

- IdtPes
- NumFis
- TecCra
- PlaVei

---

## Índices

### R088CONINDICE01

**Tipo:** Não unico

Campos:
- CraVei

### R088CONINDICE02

**Tipo:** Não unico

Campos:
- PlaVei

### R088CONINDICE03

**Tipo:** Não unico

Campos:
- IdtPes

### R088CONINDICE04

**Tipo:** Não unico

Campos:
- NumFis

---

## Relacionamentos

Nenhum relacionamento cadastrado.
