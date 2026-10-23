# R122ONB

## Descrição

Campos adicionais do candidato externo vindo do módulo Onboarding

---

## Resumo

- Campos: 6
- Chave Primária: 1 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqOnb | String(036) | Não | Contém o identificador único do campo relacionado ao candidato externo |
| NumCan | Number(007,0) | Não | Cadastro do Candidato |
| CodDep | Number(002,0) | Não | Contém o código de identificação do dependente do candidato externo |
| TipOnb | Number(001,0) | Não | Define se a informação pertence ao colaborador ou ao dependente |
| KeyOnb | String(255) | Não | Contém a chave de identificação da informação do candidato externo ou dependente |
| ValOnb | String(255) | Não | Contém o valor relacionado a informação do candidato externo ou dependente |

---

## Chave Primária

- SeqOnb

---

## Índices

### R122ONBIndice1

**Tipo:** Não unico

Campos:
- NumCan

### R122ONBIndice2

**Tipo:** Não unico

Campos:
- NumCan
- CodDep

---

## Relacionamentos

Nenhum relacionamento cadastrado.
