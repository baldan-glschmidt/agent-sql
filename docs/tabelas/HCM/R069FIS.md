# R069FIS

## Descrição

Pré Cadastro de Crachás

---

## Resumo

- Campos: 8
- Chave Primária: 4 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumCra | Number(012,0) | Não | Número do Crachá |
| TecCra | Number(001,0) | Não | Tecnologia do Crachá |
| DatAlt | Date | Não | Data início do pré-cadastro |
| HorIni | Number(005,0) | Não | Hora de início do pré-cadastro |
| DatFim | Date | Sim | Data final do pré-cadastro |
| HorFim | Number(005,0) | Sim | Hora final do pré-cadastro |
| NumFis | Number(012,0) | Sim | Número Físico do Crachá |
| CodUsu | Number(010,0) | Sim | Código do Usuário que Cadastrou Número Físico |

---

## Chave Primária

- NumCra
- TecCra
- DatAlt
- HorIni

---

## Índices

### R069FISIndice2

**Tipo:** Não unico

Campos:
- TecCra
- NumFis

### R069FISIndice3

**Tipo:** Não unico

Campos:
- NumFis

---

## Relacionamentos

Nenhum relacionamento cadastrado.
