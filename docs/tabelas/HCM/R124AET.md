# R124AET

## Descrição

Colaborador - Etapas - Anexos

---

## Resumo

- Campos: 9
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo de Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Candidato |
| CodRqu | Number(009,0) | Não | Código Requisição |
| CodEta | Number(003,0) | Não | Código Etapa |
| SeqEta | Number(003,0) | Não | Sequência Etapa |
| SeqAne | Number(002,0) | Sim | Sequência do anexo |
| NomAne | String(250) | Sim | Nome do arquivo anexo |
| ArqAne | Image | Sim | Arquivo anexo |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodRqu
- CodEta
- SeqEta

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R124AET_005

**Tabela:** R124HET

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CodRqu | CodRqu |
| CodEta | CodEta |
| SeqEta | SeqEta |

