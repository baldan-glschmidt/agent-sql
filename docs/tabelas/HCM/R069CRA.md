# R069CRA

## Descrição

Pré Cadastro de Crachás

---

## Resumo

- Campos: 16
- Chave Primária: 2 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| UsoCra | Number(002,0) | Não | Uso do Identificador do Crachá |
| NumCra | Number(012,0) | Não | Número do Crachá |
| NumCcr | Number(012,0) | Sim | Número do Cadastro no Crachá |
| CodUsu | Number(010,0) | Sim | Código do Usuário da Última Alteração |
| DatAlt | Date | Sim | Data da Última Alteração |
| PrmSab | Number(005,0) | Sim | Permissão de Acesso para os Sábados |
| PrmDom | Number(005,0) | Sim | Permissão de Acesso para os Domingos |
| PrmFer | Number(005,0) | Sim | Permissão de Acesso para os Feriados |
| CodPrm | Number(005,0) | Sim | Permissão de Acesso para os Dias Normais |
| IniAce | Number(005,0) | Sim | Início da Faixa p/ Marcação de Acesso |
| FimAce | Number(005,0) | Sim | Fim da Faixa p/ Marcação de Acesso |
| IniPto | Number(005,0) | Sim | Início da Faixa p/ Marcação de Ponto |
| FimPto | Number(005,0) | Sim | Fim da Faixa p/ Marcação de Ponto |
| MotCra | Number(002,0) | Sim | Motivo do Recebimento do Crachá |
| DatCfc | Date | Sim | Data da Confecção do Crachá |
| NumAlf | String(013) | Sim | Crachá Alfanumérico |

---

## Chave Primária

- UsoCra
- NumCra

---

## Índices

### R069CRAIndice2

**Tipo:** Unico

Campos:
- NumCra

### R069CRAIndice3

**Tipo:** Não unico

Campos:
- UsoCra
- NumCcr

---

## Relacionamentos

Nenhum relacionamento cadastrado.
