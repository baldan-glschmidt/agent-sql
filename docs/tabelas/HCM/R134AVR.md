# R134AVR

## Descrição

Turmas - Avaliação de Eficácia - Respostas

---

## Resumo

- Campos: 9
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCua | Number(009,0) | Não | Código do curso de aperfeiçoamento |
| TmaCua | Number(006,0) | Não | Código da turma |
| NumEmp | Number(004,0) | Não | Código da empresa do participante |
| TipCol | Number(001,0) | Não | Tipo colaborador participante |
| NumCad | Number(009,0) | Não | Cadastro do colaborador participante |
| CodTst | String(005) | Não | Código do Teste |
| CodPer | String(003) | Não | Código da Pergunta |
| CodRes | String(002) | Sim | Código da Resposta |
| DesRes | String(1000) | Sim | Registrar a resposta subjetiva |

---

## Chave Primária

- CodCua
- TmaCua
- NumEmp
- TipCol
- NumCad
- CodTst
- CodPer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R134AVR_001

**Tabela:** R134DTU

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| TmaCua | TmaCua |

### IR_R134AVR_005

**Tabela:** R136TES

| Origem | Destino |
|--------|---------|
| CodTst | CodTst |

### IR_R134AVR_006

**Tabela:** R136PER

| Origem | Destino |
|--------|---------|
| CodTst | CodTst |
| CodPer | CodPer |

