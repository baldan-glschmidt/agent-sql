# R304RRC

## Descrição

e-Sfinge Online - Relação do Resultado do Concurso - Complemento

---

## Resumo

- Campos: 14
- Chave Primária: 9 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| NumEdi | String(016) | Não | Número do edital de concurso |
| NumEsp | Number(006,0) | Não | Número da Especialidade |
| TipQua | Number(002,0) | Não | Tipo de Quadro |
| CarFun | String(016) | Não | Código do cargo ou função atribuído pela unidade |
| DatIni | Date | Não | Data de Início da Vigência do Cargo |
| NumCpf | Number(011,0) | Não | Número do CPF |
| NumIns | String(016) | Não | Número da Inscrição |
| SeqReg | Number(009,0) | Não | Sequência |
| NomApr | String(100) | Não | Nome do Aprovado |
| OrdGer | Number(007,0) | Não | Ordem da Classificação Geral |
| NotFin | Number(007,4) | Não | Nota Final do Aprovado |
| TipCom | Number(002,0) | Não | Tipo de complemento do resultado de concurso |
| PidSta | String(030) | Sim | Pid Status |

---

## Chave Primária

- NumEmp
- NumEdi
- NumEsp
- TipQua
- CarFun
- DatIni
- NumCpf
- NumIns
- SeqReg

---

## Índices

### R304RRCIndice1

**Tipo:** Não unico

Campos:
- PidSta

---

## Relacionamentos

Nenhum relacionamento cadastrado.
