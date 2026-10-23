# R166SOL

## Descrição

Solicitante Auxílio Educação

---

## Resumo

- Campos: 21
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatIns | Date | Não | Data de Inscrição |
| SeqSol | Number(002,0) | Não | Sequência do Solicitante |
| TipCur | String(001) | Sim | Tipo do Curso |
| CodCua | Number(009,0) | Sim | Código do Curso de Aperfeiçoamento |
| FasCua | String(003) | Sim | Fase do Curso de Aperfeiçoamento |
| CodCuf | Number(004,0) | Sim | Código do Curso de Formação |
| NivCuf | Number(002,0) | Sim | Nível de Formação do Curso |
| SeqNiv | Number(002,0) | Sim | Sequência do Nível |
| FasCuf | String(003) | Sim | Fase do Curso de Formação |
| CodOem | Number(008,0) | Sim | Código da Entidade de Ensino |
| CmpIni | Date | Sim | Competência Início da Validade do Auxílio |
| CmpFim | Date | Sim | Competência Término da Validade do Auxílio |
| SitAux | String(001) | Sim | Situação do Auxílio |
| NroAta | String(020) | Sim | Ata de Aprovação |
| ObsCbl | String(500) | Sim | Observação |
| CurIni | String(001) | Sim | Curso Requisitado Já Iniciado |
| IniCur | Date | Sim | Data de Início do Curso |
| FimCur | Date | Sim | Data de Fim do Curso |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatIns
- SeqSol

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R166SOL_012

**Tabela:** R032OEM

| Origem | Destino |
|--------|---------|
| CodOem | CodOem |

