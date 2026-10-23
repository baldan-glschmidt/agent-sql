# R134IMT

## Descrição

Turmas - Documentos

---

## Resumo

- Campos: 7
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCua | Number(009,0) | Não | Código do Curso de Aperfeiçoamento |
| TmaCua | Number(006,0) | Não | Código da Turma |
| SeqImg | Number(004,0) | Não | Sequência do Documento |
| DatArq | Date | Sim | Data do Documento |
| Imagem | Image | Sim | Arquivo |
| DesImg | String(060) | Sim | Descrição do Documento |
| NomArq | String(250) | Sim | Nome Arquivo |

---

## Chave Primária

- CodCua
- TmaCua
- SeqImg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R134IMT_000

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

