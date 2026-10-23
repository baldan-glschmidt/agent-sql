# R063ACC

## Descrição

Acesso de Vigilantes

---

## Resumo

- Campos: 11
- Chave Primária: 7 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Colaborador |
| DatAcc | Date | Não | Data do Acesso |
| HorAcc | Number(005,0) | Não | Hora do Acesso |
| CodDsp | Number(009,0) | Não | Código do Dispositivo |
| CodFnc | Number(002,0) | Não | Código da Função |
| NumCra | Number(012,0) | Sim | Número do Crachá |
| CodRon | Number(003,0) | Sim | Código da Ronda |
| SeqRon | Number(002,0) | Sim | Sequência da ronda |
| StaMon | Number(001,0) | Sim | Status do Monitoramento |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAcc
- HorAcc
- CodDsp
- CodFnc

---

## Índices

### R063ACCIndice2

**Tipo:** Não unico

Campos:
- CodRon
- SeqRon
- DatAcc
- HorAcc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
