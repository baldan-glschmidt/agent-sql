# R088DAC

## Descrição

Documentos anexos de condutores

---

## Resumo

- Campos: 8
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EmpCon | Number(004,0) | Não | Código da empresa do condutor |
| TClCon | Number(001,0) | Não | Tipo de Colaborador Condutor |
| CadCon | Number(009,0) | Não | Cadastro do Condutor |
| TipDoc | Number(004,0) | Não | Código do Tipo de Documento |
| SeqDoc | Number(006,0) | Não | Sequência Documento |
| NomArq | String(250) | Sim | Nome do Arquivo anexo |
| DocAne | Image | Sim | Documento anexo |
| ObsDoc | String(700) | Sim | Observação do Documento |

---

## Chave Primária

- EmpCon
- TClCon
- CadCon
- TipDoc
- SeqDoc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R088DAC_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| EmpCon | NumEmp |
| TClCon | TipCol |
| CadCon | NumCad |

