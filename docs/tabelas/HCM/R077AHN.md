# R077AHN

## Descrição

Avaliação de Performance - Notas

---

## Resumo

- Campos: 12
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Código do Colaborador |
| CmpAva | Date | Não | Competência da Avaliação |
| TipAva | Number(004,0) | Não | Sequência da Avaliação |
| CodHte | String(006) | Não | Código da Habilidade Técnica |
| NotAva | Number(005,2) | Sim | Nota da Habilidade |
| MetAva | Number(005,2) | Sim | Meta para a próxima avaliação |
| ComAva | String(3000) | Sim | Comentário |
| TipHab | Number(001,0) | Sim | Indica se a habilidade é Essencial ou Complementar |
| ConAva | String(001) | Sim | Indica se considera a habilidade na avaliação |
| BloHte | String(004) | Sim | Código do Bloco de Habilidades Técnicas |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CmpAva
- TipAva
- CodHte

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R077AHN_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R077AHN_005

**Tabela:** R077HTE

| Origem | Destino |
|--------|---------|
| CodHte | CodHte |

