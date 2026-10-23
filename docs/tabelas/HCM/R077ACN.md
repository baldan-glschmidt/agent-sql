# R077ACN

## Descrição

Avaliação de Conhecimentos - Notas

---

## Resumo

- Campos: 13
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Código do Colaborador |
| CmpAva | Date | Não | Competência de Geração da Avaliação |
| TipAva | Number(004,0) | Não | Sequência da Avaliação |
| FamCnc | String(004) | Não | Família do Conhecimento |
| CodCnc | String(005) | Não | Código do Conhecimento |
| NotAva | Number(005,2) | Sim | Nota da Avaliação do Conhecimento |
| VerCer | String(001) | Sim | OBSOLETO 5.4.1.39 - Assinalamento se Habilidade já foi Certificada |
| MetAva | Number(005,2) | Sim | Meta para a próxima avaliação |
| ExiRqu | String(001) | Sim | Exigência do requisito(D-Desejável/N-Necessário) |
| ComAva | String(3000) | Sim | Comentário |
| BloHte | String(004) | Sim | Código do Bloco de Habilidades Técnicas |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CmpAva
- TipAva
- FamCnc
- CodCnc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R077ACN_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R077ACN_006

**Tabela:** R125CNC

| Origem | Destino |
|--------|---------|
| FamCnc | FamCnc |
| CodCnc | CodCnc |

