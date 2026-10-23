# R038IMA

## Descrição

Histórico de Afastamemto - Documentos

---

## Resumo

- Campos: 11
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Colaborador |
| DatAfa | Date | Não | Data do Afastamento |
| HorAfa | Number(005,0) | Não | Hora do Afastamento |
| SeqImg | Number(004,0) | Não | Sequência do Documento |
| DatArq | Date | Sim | Data do Documento |
| Imagem | Image | Sim | Arquivo |
| DesImg | String(060) | Sim | Descrição do Documento |
| NomArq | String(250) | Sim | Nome Arquivo |
| CodUsu | Number(010,0) | Sim | Código do Usuário para o Colaborador |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAfa
- HorAfa
- SeqImg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
