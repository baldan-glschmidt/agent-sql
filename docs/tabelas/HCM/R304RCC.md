# R304RCC

## Descrição

e-Sfinge Online - Resultado do Concurso - Complemento

---

## Resumo

- Campos: 10
- Chave Primária: 7 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| NumEdi | String(016) | Não | Número do edital de concurso |
| NumEsp | Number(006,0) | Não | Número da especialidade |
| TipQua | Number(002,0) | Não | Tipo de quadro |
| CarFun | String(016) | Não | Código do cargo ou função atribuído pela unidade |
| DatIni | Date | Não | Data de início da vigência do cargo |
| SeqReg | Number(009,0) | Não | Sequência |
| DatHom | Date | Não | Data da homologação |
| TipCom | Number(002,0) | Não | Tipo de complemento do resultado de concurso |
| PidSta | String(030) | Sim | Pid status |

---

## Chave Primária

- NumEmp
- NumEdi
- NumEsp
- TipQua
- CarFun
- DatIni
- SeqReg

---

## Índices

### R304RCCIndice1

**Tipo:** Não unico

Campos:
- PidSta

---

## Relacionamentos

Nenhum relacionamento cadastrado.
