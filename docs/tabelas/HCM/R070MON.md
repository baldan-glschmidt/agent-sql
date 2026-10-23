# R070MON

## Descrição

Registro de Acesso

---

## Resumo

- Campos: 9
- Chave Primária: 0 campo(s)
- Índices: 3
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumCra | Number(012,0) | Sim | Número do Crachá |
| DatAcc | Date | Sim | Data do Acesso |
| HorAcc | Number(005,0) | Sim | Hora do Acesso |
| SeqAcc | Number(002,0) | Sim | Sequência do Registro |
| TipAcc | Number(003,0) | Sim | Tipo do Acesso |
| CodPlt | Number(005,0) | Sim | Código do Site |
| CodRlg | Number(005,0) | Sim | Código do Coletor no Acesso |
| CodFnc | Number(002,0) | Sim | Código da Função no Acesso |
| DirAcc | String(001) | Sim | Direção do Acesso |

---

## Chave Primária

Não possui.

---

## Índices

### R070MONIndice1

**Tipo:** Não unico

Campos:
- NumCra
- DatAcc
- HorAcc
- SeqAcc

### R070MONIndice2

**Tipo:** Não unico

Campos:
- HorAcc

### R070MONIndice3

**Tipo:** Não unico

Campos:
- DatAcc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
