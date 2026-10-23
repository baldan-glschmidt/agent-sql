# R038AET

## Descrição

Exames Toxicológicos - Anexos

---

## Resumo

- Campos: 8
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatAlt | Date | Não | Data de realização do exame toxicológico |
| SeqArq | Number(003,0) | Não | Sequência do arquivo |
| NomArq | String(250) | Sim | Nome do arquivo de anexo |
| DesArq | String(060) | Sim | Descrição do anexo |
| ArqAne | Image | Sim | Anexo |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAlt
- SeqArq

---

## Índices

### R038EATIndice1

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad

---

## Relacionamentos

Nenhum relacionamento cadastrado.
