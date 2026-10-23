# R996FLD

## Descrição

Campos do usuário

---

## Resumo

- Campos: 27
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TblNam | String(032) | Não | Nome da tabela |
| FldNam | String(032) | Não | Nome do campo |
| FldOrd | Number(005,0) | Sim | Ordem do campo no TBS |
| MskFld | String(050) | Sim | Mácara do campo |
| DatTyp | Number(002,0) | Sim | Tipo do campo |
| EnuNam | String(032) | Sim | Nome da enumeração |
| LenFld | Number(005,0) | Sim | Tamanho |
| PreFld | Number(005,0) | Sim | Precisão |
| ShrTit | String(255) | Sim | Título curto |
| LgnTit | String(255) | Sim | Título longo |
| DesFld | String(255) | Sim | Descrição |
| CanNul | Number(001,0) | Sim | Permite nulo |
| CodHlp | Number(005,0) | Sim | Código da ajuda |
| ValDef | String(255) | Sim | Valor padrão |
| OwnMod | String(007) | Sim | Módulos proprietários |
| FldDep | String(099) | Sim | Campos dependentes separados por ; |
| CodUsu | Number(010,0) | Sim | Código do usuário |
| OriNam | String(032) | Sim | Nome do campo original, no caso de renomear |
| LasUpd | Date | Sim | Data da última alteração |
| ReqFld | String(001) | Sim | Define se o campo é obrigatório |
| ObjSis | String(001) | Sim | Identifica se o campo é de sistema ou usuário |
| MEMKND | Number(004,0) | Sim | Tipo do Campo |
| KEPVAL | String(001) | Sim | Mantém Valor |
| ALLOWINSTT | String(001) | Sim | Permite Inserção na Tabela de Destino |
| AUTINC | String(001) | Sim | Possui Auto Incremento |
| DEPEON | String(255) | Sim | Dependências |
| INCRMT | String(004) | Sim | Valor do Incremento usado no autoincremento |

---

## Chave Primária

- TblNam
- FldNam

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
