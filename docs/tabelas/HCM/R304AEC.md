# R304AEC

## Descrição

e-Sfinge Online - Arquivos do Edital do Concurso/Processo Seletivo

---

## Resumo

- Campos: 8
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| NumEdi | String(016) | Não | Número do edital de concurso |
| NomArq | String(100) | Não | Nome do arquivo relacionado ao concurso |
| SeqReg | Number(009,0) | Não | Sequência |
| NatArq | Number(002,0) | Sim | Natureza do arquivo texto |
| UrlArq | String(1000) | Sim | URL do arquivo (se disponível online) |
| ArqDoc | Image | Sim | Arquivo do documento |
| PidSta | String(030) | Sim | Pid Status |

---

## Chave Primária

- NumEmp
- NumEdi
- NomArq
- SeqReg

---

## Índices

### R304AECIndice1

**Tipo:** Não unico

Campos:
- PidSta

---

## Relacionamentos

Nenhum relacionamento cadastrado.
